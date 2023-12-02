inp = [*map(lambda x: int(x), open(0).read().strip().splitlines())]

c = 0

for i, n in enumerate(inp[:-1]):
    if n < inp[i+1]: c += 1

print(c)

c = 0

for i in range(len(inp)):
    if sum(inp[i:i+3]) < sum(inp[i+1:i+4]): c += 1

    #Merk: [x:y:z] x er inklusiv start, y er **eksklusiv** slutt, z er steg og retning.

print(c)