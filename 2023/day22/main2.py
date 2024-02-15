from collections import deque


class Brick:
    def __init__(self, sx, sy, sz, ex, ey, ez):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.ex = ex
        self.ey = ey
        self.ez = ez

        self.supports = []
        self.supportedBy = []

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
    q = deque(b for b in brick.supports if len(b.supportedBy) == 1)
    falling = set(q)

    while q:
        b1 = q.popleft()
        for b2 in set(b1.supports) - falling:
            if set(b2.supportedBy) <= falling:
                q.append(b2)
                falling.add(b2)

    total += len(falling)

print(total)
