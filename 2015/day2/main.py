lines = open(0).read().strip().splitlines()



t = 0

for line in lines:
    l, w, h = [int(x) for x in line.split('x')]
    t += 2*l*w + 2*l*h + 2*w*h + min(l*w, l*h, w*h)

print(t)

r = 0

for line in lines:
    l, w, h = [int(x) for x in line.split('x')]
    short = [l, w, h]
    short.remove(max(l, w, h))
    r += 2*short[0] + 2*short[1] + l*w*h

print(r)