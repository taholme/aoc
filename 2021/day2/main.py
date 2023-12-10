x, y = 0, 0

for line in open(0).read().strip().splitlines():
    dr, ln = line.split()
    ln = int(ln)

    if dr == "forward":
        x += ln
    elif dr == "down":
        y += ln
    else:
        y -= ln
print(x * y)
