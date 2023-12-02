inp = open(0).read().strip().splitlines()

NUM_STRINGS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total = 0
for line in inp:
    line = line.strip()
    first = None
    last = None

    curr_string = ""

    for c in line:
        if c.isdigit():
            if first is None:
                first = int(c)
            last = int(c)
            curr_string = ""
            continue

        curr_string += c
        for itx, num in enumerate(NUM_STRINGS):
            if num in curr_string:
                if first is None:
                    first = itx + 1
                last = itx + 1
                curr_string = curr_string[-1]
                break

    val = first * 10 + last
    print(val)
    total += val
print(f"Part 2: {total}")

