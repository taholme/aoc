card, door = list(map(int, open(0).read().strip().splitlines()))

loop_size, val = 0, 1
while val != card:
    val = (val * 7) % 20201227
    loop_size += 1

print(pow(door, loop_size, 20201227))
