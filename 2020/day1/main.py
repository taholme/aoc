inp = [*map(lambda x: int(x), open(0).read().strip().splitlines())]

for i, n in enumerate(inp):
    for m in inp[i+1:]:
        if n+m == 2020:
            print(n*m)
            break
    else:
        continue
    break

for i, n in enumerate(inp):
    for m in inp[i+1:]:
        for o in inp[i+1:]:
            if n+m+o == 2020:
                print(n*m*o)
                break
        else:
            continue
        break
    else:
        continue
    break