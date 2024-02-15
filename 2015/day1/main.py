pinput = open(0).read().strip()

print(sum(1 if char == "(" else -1 for char in pinput))

# Task 2

c = 0

for i, char in enumerate(pinput):
    c += 1 if char == "(" else -1
    if c == -1:
        print(i + 1)
        break
