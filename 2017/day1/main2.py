inp = open(0).read().strip()

t = 0

fl = len(inp)
hl = fl // 2

for i, n in enumerate(inp):
    if n == inp[(i+hl) % fl]:
        t += int(n)

print(t)