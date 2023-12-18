outline = [(0, 0)]
dirs = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
boundary_points = 0

for line in open(0):
    dir, ln, clr = line.split()
    ln = int(ln)
    dr, dc = dirs[dir]
    r, c = outline[-1]
    boundary_points += ln
    outline.append((r + dr * ln, c + dc * ln))

A = (
    abs(
        sum(
            outline[i][0] * (outline[i - 1][1] - outline[(i + 1) % len(outline)][1])
            for i in range(len(outline))
        )
    )
    // 2
)

i = A - boundary_points // 2 + 1

print(i + boundary_points)
