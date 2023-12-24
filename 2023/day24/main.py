from itertools import combinations
from sympy import symbols, solve

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open(0)]

total = 0

for (sx1, sy1, _, vx1, vy1, _), (sx2, sy2, _, vx2, vy2, _) in combinations(
    hailstones, 2
):
    px, py = symbols("px py")
    answers = solve(
        [vy1 * (px - sx1) - vx1 * (py - sy1), vy2 * (px - sx2) - vx2 * (py - sy2)]
    )
    if answers == []:
        continue
    x, y = answers[px], answers[py]
    if (
        200000000000000 <= x <= 400000000000000
        and 200000000000000 <= y <= 400000000000000
    ):
        if ((x - sx1) * vx1 >= 0 and (y - sy1) * vy1 >= 0) and (
            (x - sx2) * vx2 >= 0 and (y - sy2) * vy2 >= 0
        ):
            total += 1

print(total)  # 1m23.883s
