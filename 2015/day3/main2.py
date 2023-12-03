
coord1 = coord2 = 0 + 0j
seen = set([coord1])

for i, c in enumerate(open(0).read()):
    if i % 2 == 0:
        if c == '>':
            coord1 += 1
        elif c == '<':
            coord1 -= 1
        elif c == '^':
            coord1 += 1j
        else:
            coord1 -= 1j
        seen.add(coord1)
    else:
        if c == '>':
            coord2 += 1
        elif c == '<':
            coord2 -= 1
        elif c == '^':
            coord2 += 1j
        else:
            coord2 -= 1j
        seen.add(coord2)

print(len(seen))