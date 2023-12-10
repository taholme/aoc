inp = [*map(lambda x: int(x), open(0).read().strip().splitlines())]

fuelcalc = lambda x: x // 3 - 2

print(sum(map(fuelcalc, inp)))


def recurfuelcalc(x):
    res = x
    t = []
    while fuelcalc(res) > 0:
        res = fuelcalc(res)
        t.append(res)
    return sum(t)


print(sum(map(recurfuelcalc, inp)))
