from collections import deque

G = open(0).read().strip().splitlines()
R = len(G)
C = len(G[0])


for r, row in enumerate(G):
    for c, ch in enumerate(row):
        if ch == "S":
            sr, sc = (r, c)


ans = set()
seen = {(sr, sc)}
q = deque([(sr, sc, 64)])

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

print(len(ans))
