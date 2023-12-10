x = 1
val = []

for inst in open(0).read().strip().splitlines():
    if inst == "noop":
        val.append(x)
    else:
        new_x = int(inst.split()[1])
        val.append(x)
        val.append(x)
        x += new_x

for i in range(0, len(val), 40):
    for j in range(40):
        print("##" if abs(val[i + j] - j) <= 1 else "  ", end="")
    print()
