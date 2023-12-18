grid = tuple(open(0).read().splitlines())

def cycle():
    global grid
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)

seen = set(grid)
array = list([grid])

i = 0

while True:
    i += 1
    cycle()
    if grid in seen:
        break
    seen.add(grid)
    array.append(grid)
    
first = array.index(grid)
    
grid = array[(1000000000 - first) % (i - first) + first]

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))