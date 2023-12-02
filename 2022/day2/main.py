t = 0

for line in open(0):
    m, n = map(ord, line.split())
    m -= ord('A')
    n -= ord('X')

    t += n+1
    if m == (n-1) % 3:
        t += 6
    elif m == n:
        t += 3
print(t)