inp = open(0).read().strip().split(', ')

pos = 0 + 0j
rot = 0 + 1j # starter Nord -> påvirker y-aksen
known = {pos}

for d in inp:
    r, l = d[0], int(d[1:])
    if r == 'R':
        rot *= -1j
    else:
        rot *= 1j
    for i in range(l):
        pos += 1 * rot
        if pos in known:
            print(abs(pos.real) + abs(pos.imag))
            break
        else:
            known.add(pos)
    else:
        continue
    break