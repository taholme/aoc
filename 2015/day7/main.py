from collections import defaultdict
import re

lines = open(0).read().strip().splitlines()

wires = defaultdict(int)
conv = lambda x: int(x) if x.isdigit() else x

operations = {
    "OR": lambda a, b: a | b,
    "AND": lambda a, b: a & b,
    "LSHIFT": lambda a, b: a << b,
    "RSHIFT": lambda a, b: a >> b,
    "NOT": lambda *a: ~a[0],
}

for line in lines:
    command = re.findall(rf"({'|'.join(operations.keys())})", line)
    args = [*map(conv, re.findall("([a-z0-9]+)", line))]
    destination = args.pop()
    print(line, command, args, destination)
    wires[destination] = (
        (lambda arg: operations[command[0]](wires[arg[0]], wires[arg[-1]]))
        if len(command)
        else wires[args[0]]
    )

print(wires["d"])
