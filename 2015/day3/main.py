
coord = 0 + 0j
seen = set([coord])

for c in open(0).read():
    if c == '>':
        coord += 1
    elif c == '<':
        coord -= 1
    elif c == '^':
        coord += 1j
    else:
        coord -= 1j
    seen.add(coord)

print(len(seen))