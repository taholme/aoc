outline = [(0, 0)]
dirs = {"3": (-1, 0), "1": (1, 0), "0": (0, 1), "2": (0, -1)}
boundary_points = 0

for line in open(0):
    _, _, clr = line.split()
    ln = int(clr[2:-2], base=16)
    dr, dc = dirs[clr[-2]]
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
