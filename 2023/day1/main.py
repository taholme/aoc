import re

lines = open(0).read().strip().splitlines()

t = 0
for line in lines:
    nums = re.findall(r"(\d)", line)
    t += int(nums[0] + nums[-1])

t2 = 0
n = "one two three four five six seven eight nine".split()
p = "(?=(" + "|".join(n) + "|\\d))"
con = lambda x: str(n.index(x) + 1) if not x.isdigit() else x

for line in lines:
    nums = re.findall(p, line)
    print(nums)
    t2 += int(con(nums[0]) + con(nums[-1]))

print(t)
print(t2)
