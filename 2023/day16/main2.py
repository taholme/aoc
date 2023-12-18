from collections import deque
grid = open(0).read().splitlines()

def solve(r, c, dr, dc):
    def addToSeenAndQueue(r,c,dr,dc):
        if (r, c, dr, dc) not in seen:
            seen.add((r, c, dr, dc))
            q.append((r, c, dr, dc))
    seen = set()
    q = deque([(r, c, dr, dc)])

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
                    
    return len({(r, c) for (r, c, _, _) in seen})

max_val = 0

for r in range(len(grid)):
    max_val = max(max_val, solve(r, -1, 0, 1))
    max_val = max(max_val, solve(r, len(grid[0]), 0, -1))
    
for c in range(len(grid)):
    max_val = max(max_val, solve(-1, c, 1, 0))
    max_val = max(max_val, solve(len(grid), c, -1, 0))

print(max_val)