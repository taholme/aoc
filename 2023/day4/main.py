lines = open(0).read().strip().splitlines()

t = 0

for line in lines:
    c = 0
    line = line.split(": ")[1]
    winning, card = line.split(" | ")
    winning = list(map(int, winning.split()))
    card = list(map(int, card.split()))

    for num in card:
        if num in winning:
            if c:
                c *= 2
            else:
                c = 1
    t += c
print(t)
