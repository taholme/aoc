import re

lines = open(0).read().strip().splitlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]

t = 0

for line in lines:
    com, sx, sy, ex, ey = re.findall(
        r"(toggle|on|off) (\d+),(\d+) through (\d+),(\d+)", line
    )[0]
    for r in range(int(sx), int(ex) + 1):
        for c in range(int(sy), int(ey) + 1):
            if com == "off":
                grid[r][c] = 0
            elif com == "on":
                grid[r][c] = 1
            elif com == "toggle":
                grid[r][c] = not grid[r][c]

for row in grid:
    t += sum(row)

print(t)

grid = [[0 for _ in range(1000)] for _ in range(1000)]

t = 0

for line in lines:
    com, sx, sy, ex, ey = re.findall(
        r"(toggle|on|off) (\d+),(\d+) through (\d+),(\d+)", line
    )[0]
    for r in range(int(sx), int(ex) + 1):
        for c in range(int(sy), int(ey) + 1):
            if com == "off":
                grid[r][c] -= 0 if grid[r][c] == 0 else 1
            elif com == "on":
                grid[r][c] += 1
            elif com == "toggle":
                grid[r][c] += 2

for row in grid:
    t += sum(row)

print(t)
