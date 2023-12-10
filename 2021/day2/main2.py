x, y, aim = 0, 0, 0

for line in open(0).read().strip().splitlines():
    dr, ln = line.split()
    ln = int(ln)

    if dr == "forward":
        x += ln
        y += ln * aim
    elif dr == "down":
        aim += ln
    else:
        aim -= ln
print(x * y)
