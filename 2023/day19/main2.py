from math import prod

b1 = open(0).read().strip().split("\n\n")[0].splitlines()

workflows = {}

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


def count(ranges, name="in"):
    if name == "R":
        return 0
    if name == "A":
        return prod([hi - lo + 1 for lo, hi in ranges.values()])

    rules, fallback = workflows[name]

    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == "<":
            T = (lo, min(n - 1, hi))
            F = (max(n, lo), hi)
        else:
            T = (max(n + 1, lo), hi)
            F = (lo, min(n, hi))
        if T[0] <= T[1]:
            copy = {**ranges}
            copy[key] = T
            total += count(copy, target)
        if F[0] <= F[1]:
            ranges = {**ranges}
            ranges[key] = F
        else:
            break
    else:
        total += count(ranges, fallback)

    return total


print(count({key: (1, 4000) for key in "xmas"}))
