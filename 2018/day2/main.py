from collections import Counter
from itertools import combinations

lines = open(0).read().strip().splitlines()

print(
    (lambda a, b: a * b)(
        *[sum(1 for l in lines if x in Counter(l).values()) for x in (2, 3)]
    )
)
print(
    (lambda a, b: "".join([a[i] for i in range(len(a)) if a[i] == b[i]]))(
        *[
            l
            for l in combinations(lines, 2)
            if sum(1 for i in range(len(l[0]) - 1) if l[0][i] != l[1][i]) < 2
        ][0]
    )
)
