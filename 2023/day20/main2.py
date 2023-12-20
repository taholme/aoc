from collections import deque
from math import lcm


class Module:
    def __init__(self, name, type, targets):
        self.name = name
        self.type = type
        self.targets = targets

        if type == "%":
            self.memory = 0
        else:
            self.memory = {}

    def __repr__(self):
        return f"{self.name}({self.type=},{self.targets=},{str(self.memory)=})"


modules = {}
broadcast_targets = []

for line in open(0):
    left, right = line.strip().split(" -> ")
    targets = right.split(", ")
    if left == "broadcaster":
        broadcast_targets = targets
    else:
        type = left[0]
        name = left[1:]
        modules[name] = Module(name, type, targets)

for name, module in modules.items():
    for output in module.targets:
        if output in modules and modules[output].type == "&":
            modules[output].memory[name] = 0

final_machine = [name for name, module in modules.items() if "rx" in module.targets][0]
cycle_len = {}
seen = {name: 0 for name, module in modules.items() if final_machine in module.targets}

index = 0

while True:
    index += 1
    q = deque([("broadcaster", x, 0) for x in broadcast_targets])

    while q:
        source, target, pulse = q.popleft()

        if target not in modules:
            continue

        module = modules[target]

        if module.name == final_machine and pulse == 1:
            seen[source] += 1

            if source not in cycle_len:
                cycle_len[source] = index

                if all(seen.values()):
                    print(lcm(*cycle_len.values()))
                    exit(0)

        if module.type == "%":
            if pulse == 0:
                module.memory = 1 if module.memory == 0 else 0
                outgoing = 1 if module.memory == 1 else 0
                for target in module.targets:
                    q.append((module.name, target, outgoing))
        else:
            module.memory[source] = pulse
            outgoing = 0 if all(x == 1 for x in module.memory.values()) else 1
            for target in module.targets:
                q.append((module.name, target, outgoing))
