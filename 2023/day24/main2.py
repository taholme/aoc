from operator import itemgetter
from sympy import symbols, solve

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open(0)]

xr, yr, zr, vxr, vyr, vzr = symbols("xr yr zr vxr vyr vzr")

intersections = []

for sx, sy, sz, vx, vy, vz in hailstones:
    intersections.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    intersections.append((xr - sx) * (vz - vzr) - (zr - sz) * (vx - vxr))

print(sum(itemgetter(xr, yr, zr)(solve(intersections, dict=True)[0])))
