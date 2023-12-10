inp = [*map(lambda x: int(x), open(0).read().strip().splitlines())]

print(sum(inp))


t = 0
known = set()

while True:
    for i in inp:
        if t in known:
            print(t)
            break
        known.add(t)
        t += i
    else:
        continue
    break
