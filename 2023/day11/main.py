grid = open(0).read().strip().splitlines()

empty_rows = [r for r, row in enumerate(grid) if all(ch == "." for ch in row)]
empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch == "." for ch in col)]

stars = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"]

total = 0
expansion = 1000000  # 2 for part 1

for i, x in enumerate(stars):
    for y in stars[:i]:
        for r in range(min(x[0], y[0]), max(x[0], y[0])):
            total += 1 if r not in empty_rows else expansion
        for c in range(min(x[1], y[1]), max(x[1], y[1])):
            total += 1 if c not in empty_cols else expansion

print(total)
