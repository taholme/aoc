import re

lines = open(0).read().strip().splitlines()

t = 0

for line in lines:
    vowels = re.findall("(a|e|i|o|u)", line)
    doubleletters = re.findall(r"([a-z])\1", line)
    bad_words = re.findall("(ab|cd|pq|xy)", line)
    if len(doubleletters) < 1:
        continue
    if len(vowels) < 3:
        continue
    if len(bad_words) > 0:
        continue
    t += 1

print(t)

t = 0

for line in lines:
    doubleletters = re.findall(r"(\w{2}).*?(\1)", line)
    palindrome = re.findall(r"(?:(\w)(\w)\1)", line)
    if len(doubleletters) < 1:
        continue
    if len(palindrome) < 1:
        continue
    t += 1

print(t)
