from collections import deque
grid = open(0).read().splitlines()

seen = set()
# r, c, dr, dc
q = deque([(0, -1, 0, 1)])

def addToSeenAndQueue(r,c,dr,dc):
    if (r, c, dr, dc) not in seen:
        seen.add((r, c, dr, dc))
        q.append((r, c, dr, dc))

while q:
    r, c, dr, dc = q.popleft()
    r += dr
    c += dc
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        continue
    ch = grid[r][c]
    if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
        addToSeenAndQueue(r,c,dr,dc)
    elif ch == "/":
        dr, dc = -dc, -dr
        addToSeenAndQueue(r,c,dr,dc)
    elif ch == "\\":
        dr, dc = dc, dr
        addToSeenAndQueue(r,c,dr,dc)
    else:
        for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
            addToSeenAndQueue(r,c,dr,dc)
                
print(len({(r, c) for (r, c, _, _) in seen}))