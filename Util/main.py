from copy import deepcopy
from math import gcd, lcm
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify

D = open(0).read().strip()
L = D.splitlines()  # .split('\n\n')
G = [[c for c in row] for row in L]
R = len(G)
C = len(G[0])
