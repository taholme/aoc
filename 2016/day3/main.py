lines = open(0).read().strip().splitlines()

t = 0

for line in lines:
    a, b, c = map(int, line.strip().split())
    if a + b > c and a + c > b and b + c > a:
        t += 1

print(t)

t = 0

for i in range(0, len(lines), 3):
    a1, b1, c1 = map(int, lines[i].strip().split())
    a2, b2, c2 = map(int, lines[i + 1].strip().split())
    a3, b3, c3 = map(int, lines[i + 2].strip().split())
    if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
        t += 1
    if b1 + b2 > b3 and b1 + b3 > b2 and b2 + b3 > b1:
        t += 1
    if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
        t += 1

print(t)
