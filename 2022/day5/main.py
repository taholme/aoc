import re
crates, instructions = open(0).read().split('\n\n')
instructions = instructions.split('\n')

s = [crate[1::4] for crate in crates.split('\n')]
s.pop()
s = [list("".join(c).strip()[::-1]) for c in zip(*s)]

print(s)

for inst in instructions:
    a, b, c = map(int, re.findall(r"move (\d+) from (\d+) to (\d+)", inst)[0])
    s[c - 1].extend(s[b - 1][-a:][::-1])
    s[b - 1] = s[b - 1][:-a]

print("".join([a[-1] for a in s]))