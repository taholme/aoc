import re
lines = open(0).read().strip().splitlines()

rmax, gmax, bmax = 12, 13, 14

t = 0

for i, line in enumerate(lines):
    gid = re.findall('Game (\\d+)', line)
    r = max(map(int,re.findall('(\\d+) red', line)))
    g = max(map(int,re.findall('(\\d+) green', line)))
    b = max(map(int,re.findall('(?=(\\d+) blue)', line)))
    t += r*g*b
    # if sum(r) < rmax and sum(g) < gmax and sum(b) < bmax:
    #     t+= i+1
print(t)