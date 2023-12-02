t = 0

for line in open(0):
    m, n = map(ord, line.split())
    m -= ord('A')
    n -= ord('X')

    if n == 1:
        t += 3 + m + 1
    elif n == 0:
        t += (m-1) % 3 + 1
    else:
        t += 6 + ((m+1) % 3) + 1
print(t)