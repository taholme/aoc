# times, distances = [list(map(int,line.split(":")[1].split())) for line in open(0)]
times, distances = [
    list(map(int, ["".join(line.split(":")[1].split())])) for line in open(0)
]

t = 1

for time, distance in zip(times, distances):
    margin = sum(wait * (time - wait) > distance for wait in range(time))
    if margin > 0:
        t *= margin

print(t)
