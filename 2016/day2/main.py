numpad = [[y for y in range(x*3+1,x*3+4)] for x in range(3)]

r, c = 1, 1

o = ""

for line in open(0).read().strip().splitlines():
    for char in line:
        match char:
            case "U":
                r -= 1 if r-1 >= 0 else 0
            case "D":
                r += 1 if r+1 < len(numpad) else 0
            case "R":
                c += 1 if c+1 < len(numpad[0]) else 0
            case "L":
                c -= 1 if c-1 >= 0 else 0
    o += str(numpad[r][c])

print(o)
