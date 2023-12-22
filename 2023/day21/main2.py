from collections import deque

G = open(0).read().strip().splitlines()
R = len(G)
C = len(G[0])
STEPS = 26501365


for r, row in enumerate(G):
    for c, ch in enumerate(row):
        if ch == "S":
            sr, sc = (r, c)

# print(R, C, R == C)
# print(sr, sc, R // 2, sr == sc == R // 2)
# print(STEPS % R, R // 2, STEPS % R == R // 2)


def fill(sr, sc, s):
    ans = set()
    seen = {(sr, sc)}
    q = deque([(sr, sc, s)])

    while q:
        r, c, steps = q.popleft()

        if steps % 2 == 0:
            ans.add((r, c))
        if steps == 0:
            continue

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (
                nr < 0
                or nr >= R
                or nc < 0
                or nc >= C
                or G[nr][nc] == "#"
                or (nr, nc) in seen
            ):
                continue
            seen.add((nr, nc))
            q.append((nr, nc, steps - 1))

    return len(ans)


extended_grid_width = STEPS // R - 1
odd = (extended_grid_width // 2 * 2 + 1) ** 2
even = ((extended_grid_width + 1) // 2 * 2) ** 2

odd_points = fill(sr, sc, 129)
even_points = fill(sr, sc, 130)

edge_t = fill(R - 1, sc, R - 1)
edge_r = fill(sr, 0, R - 1)
edge_b = fill(0, sc, R - 1)
edge_l = fill(sr, R - 1, R - 1)

small_tr = fill(R - 1, 0, R // 2 - 1)
small_tl = fill(R - 1, R - 1, R // 2 - 1)
small_br = fill(0, 0, R // 2 - 1)
small_bl = fill(0, R - 1, R // 2 - 1)

large_tr = fill(R - 1, 0, R * 3 // 2 - 1)
large_tl = fill(R - 1, R - 1, R * 3 // 2 - 1)
large_br = fill(0, 0, R * 3 // 2 - 1)
large_bl = fill(0, R - 1, R * 3 // 2 - 1)

print(
    odd * odd_points
    + even * even_points
    + edge_t
    + edge_r
    + edge_b
    + edge_l
    + (extended_grid_width + 1) * (small_tr + small_tl + small_br + small_bl)
    + extended_grid_width * (large_tr + large_tl + large_br + large_bl)
)
