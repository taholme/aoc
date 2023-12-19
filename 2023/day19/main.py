b1, b2 = [x.splitlines() for x in open(0).read().strip().split("\n\n")]

workflows = {}

ops = {
    ">": lambda a, b: a > b,
    "<": lambda a, b: a < b,
}

for line in b1:
    label, rest = line.split("{")
    *maps, fallback = rest[:-1].split(",")
    workflows[label] = ([], fallback)
    for map in maps:
        comparison, target = map.split(":")
        key = comparison[0]
        cmp = comparison[1]
        n = int(comparison[2:])
        workflows[label][0].append((key, cmp, n, target))


def validate(item, name="in"):
    if name == "R":
        return False
    if name == "A":
        return True
    rules, fallback = workflows[name]

    for key, cmp, n, target in rules:
        if ops[cmp](item[key], n):
            return validate(item, target)

    return validate(item, fallback)


total = 0

for line in b2:
    item = {}
    for section in line[1:-1].split(","):
        ch, val = section.split("=")
        item[ch] = int(val)
    if validate(item):
        total += sum(item.values())

print(total)
