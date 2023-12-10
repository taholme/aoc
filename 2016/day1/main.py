inp = open(0).read().strip().split(", ")

pos = 0 + 0j
rot = 0 + 1j  # starter Nord -> påvirker y-aksen

for d in inp:
    r, l = d[0], int(d[1:])
    if r == "R":
        rot *= -1j
    else:
        rot *= 1j
    pos += l * rot

print(abs(pos.real) + abs(pos.imag))
