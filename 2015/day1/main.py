pinput = open(0).read().strip()

# Task 1
c = 0

for char in pinput:
    c += 1 if char == "(" else -1

print(c)

# Task 2

c = 0

for i, char in enumerate(pinput):
    c += 1 if char == "(" else -1
    if c == -1:
        print(i + 1)
        break
