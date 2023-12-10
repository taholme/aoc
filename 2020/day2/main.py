import re

lines = open(0).read().strip().splitlines()


print(
    sum(
        1
        for line in lines
        for s, e, l, p in re.findall(r"(\d+)-(\d+) (\w): (\w+)", line)
        if p.count(l) in range(int(s), int(e) + 1)
    )
)
# print(sum(1 for line in lines for start, end, letter, password in re.findall(r"(\d+)-(\d+) (\w): (\w+)", line) if password.count(letter) in range(int(start), int(end)+1)))

print(
    sum(
        1
        for line in lines
        for i1, i2, letter, password in re.findall(r"(\d+)-(\d+) (\w): (\w+)", line)
        if password[int(i1)] == letter or password[int(i2)] == letter
    )
)
