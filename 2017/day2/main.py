from itertools import combinations

rows = [
    sorted(list(map(int, line.split()))) for line in open(0).read().strip().splitlines()
]

print(sum(b - a for a, *_, b in rows))
print(sum(b // a for row in rows for a, b in combinations(row, 2) if b % a == 0))
