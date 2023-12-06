from collections import Counter
from itertools import combinations
lines = open(0).read().strip().splitlines()

print(sum(all(x == 1  for x in Counter(line.split()).values()) for line in lines))
print(sum(all(Counter(a) != Counter(b) for a, b in combinations([set(x) for x in line.split()], 2)) for line in lines))
#Forventet output av test skal være 3, men får 2, får rikitg på input
