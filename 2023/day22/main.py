class Brick:
    def __init__(self, sx, sy, sz, ex, ey, ez):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.ex = ex
        self.ey = ey
        self.ez = ez

        self.supports = list()
        self.supportedBy = list()

    def __repr__(self):
        return f"Start: {self.sx, self.sy, self.sz}, End: {self.ex, self.ey, self.ez}"


bricks = []

for line in open(0).read().strip().splitlines():
    (sx, sy, sz), (ex, ey, ez) = [
        list(map(int, part.split(","))) for part in line.split("~")
    ]
    bricks.append(Brick(sx, sy, sz, ex, ey, ez))
bricks.sort(key=lambda brick: brick.sz)

intersects = lambda a, b: max(a.sx, b.sx) <= min(a.ex, b.ex) and max(a.sy, b.sy) <= min(
    a.ey, b.ey
)

for i, brick in enumerate(bricks):
    maxz = 1
    for check in bricks[:i]:
        if intersects(brick, check):
            maxz = max(maxz, check.ez + 1)
    brick.ez -= brick.sz - maxz
    brick.sz = maxz

bricks.sort(key=lambda brick: brick.sz)

for i, brick in enumerate(bricks):
    for check in bricks[:i]:
        if intersects(brick, check) and brick.sz == check.ez + 1:
            brick.supportedBy.append(check)
            check.supports.append(brick)


total = 0

for brick in bricks:
    if all(len(b.supportedBy) >= 2 for b in brick.supports):
        total += 1
print(total)
