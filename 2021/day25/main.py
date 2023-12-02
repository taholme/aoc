grid = open(0).read().strip().splitlines()

R = len(grid)
C = len(grid[0])

east = []
south = []

for r in range(R):
    for c in range(C):
        if grid[r][c] == '>':
            east.append([r,c])
        elif grid[r][c] == 'v':
            south.append([r,c])

taken = [[col != '.' for col in row] for row in grid]

def move(herd, dr, dc):
    m = [x for x in herd if not taken[(x[0]+dr) % R][(x[1]+dc) % C]]
    for x in m:
        r, c = x

        x[0] = (r+dr) % R
        x[1] = (c+dc) % C

        taken[r][c] = False
        taken[x[0]][x[1]] = True
    return len(m)

i = 0
while True:
    i += 1
    if not move(east, 0, 1) + move(south, 1, 0):
        break
print(i)