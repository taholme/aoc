inp = open(0).read().strip()

t = 0

for i, n in enumerate(inp):
    if i != len(inp)-1:
        if n == inp[i+1]:
            t += int(n)
    else:
        if n == inp[0]:
            t += int(n)
print(t)

