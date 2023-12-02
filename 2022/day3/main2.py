t = 0

while True:
    try:
        x = input()
        y = input()
        z = input()
    except:
        break

    k, = set(x) & set(y) & set(z)
    t += ord(k) - (96 if ord(k) >= 97 else 38)

print(t)
