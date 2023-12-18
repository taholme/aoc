lines = open(0).read().strip().split(',')
t = 0
for line in lines:
    curr = 0
    for ch in line:
        curr += ord(ch)
        curr *= 17
        curr %= 256
    t += curr

print(t)



        
