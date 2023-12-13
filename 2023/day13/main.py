def row_symmetry(grid):
    for r in range(1, len(grid)):
        top = grid[:r][::-1]
        bot = grid[r:]

        top = top[: len(bot)]
        bot = bot[: len(top)]

        if top == bot:
            return r
    return 0


total = 0

for block in open(0).read().strip().split("\n\n"):
    grid = block.splitlines()

    row = row_symmetry(grid)
    col = row_symmetry(list(zip(*grid)))

    total += row * 100
    total += col

print(total)
