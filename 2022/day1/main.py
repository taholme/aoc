inp = [
    sum(y)
    for y in [map(int, x.split("\n")) for x in open(0).read().strip().split("\n\n")]
]

print(max(inp))
inp.sort()
print(sum(inp[-3:]))
