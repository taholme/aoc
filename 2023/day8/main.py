import re
instructions, maps = open(0).read().strip().split('\n\n')

maps = maps.splitlines()

d = {}
for m in maps:
    a, b, c = re.findall(r'(\w+) = \((\w+), (\w+)\)', m)[0]
    # print(f"d[{a}] = ({b}, {c})")
    d[a] = (b,c)

cnt = 0
mover = 'AAA'

while mover != "ZZZ":
    for char in instructions:
        cnt += 1
        mover = d[mover][0 if char == "L" else 1]

print(cnt)