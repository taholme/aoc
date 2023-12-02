t = 0
for line in open(0):
    x = set(line[0:len(line)//2]) & set(line[len(line)//2:])
    ordval = [ord(c) for c in x][0]
    t += ordval - (96 if ordval >= 97 else 38)
print(t)
    # print([ord(c) for c in x][0] - ord('A'))