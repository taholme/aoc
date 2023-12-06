x = 1
val = [0]

for inst in open(0).read().strip().splitlines():
    if inst == 'noop':
        val.append(x)
    else:
        new_x = int(inst.split()[1])
        val.append(x)
        val.append(x)
        x += new_x
val.append(x)


print(sum(a*b for a,b in list(enumerate(val))[20::40]))