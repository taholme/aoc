grid = [row.strip()[1:-1] for row in open(0).readlines()]

R = len(grid)
C = len(grid[0])

start = (0, 0)
end = (R - 1, C - 1)

points = [start, end]


def is_valid(nr, nc):
    return 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#"


for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "#":
            continue
        neighbors = sum(bool(is_valid(nr, nc))
                    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])
        if neighbors >= 3:
            points.append((r, c))

adjacencies = {point: {} for point in points}

for point in points:
    filo = [(0, *point)]
    seen = {point}

    while filo:
        n, r, c = filo.pop()

        if n != 0 and (r, c) in points:
            adjacencies[point][(r, c)] = n
            continue

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            if is_valid(nr, nc) and (nr, nc) not in seen:
                filo.append((n + 1, nr, nc))
                seen.add((nr, nc))

seen = set()


def dfs(point):
    if point == end:
        return 0

    m = -(10**9)

    seen.add(point)
    for nx in adjacencies[point]:
        if nx not in seen:
            m = max(m, dfs(nx) + adjacencies[point][nx])
    seen.remove(point)

    return m


print(dfs(start))
