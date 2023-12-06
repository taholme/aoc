numpad = [['.', '.', '1', '.', '.'],
          ['.', '2', '3', '4', '.'],
          ['5', '6', '7', '8', '9'],
          ['.', 'A', 'B', 'C', '.'],
          ['.', '.', 'D', '.', '.']]

r, c = 2, 0

o = ""

for line in open(0).read().strip().splitlines():
    for char in line:
        match char:
            case "U":
                r -= 1 if r-1 >= 0 and numpad[r-1][c] != '.' else 0
            case "D":
                r += 1 if r+1 < len(numpad) and numpad[r+1][c] != '.' else 0
            case "R":
                c += 1 if c+1 < len(numpad[0]) and numpad[r][c+1] != '.' else 0
            case "L":
                c -= 1 if c-1 >= 0 and numpad[r][c-1] != '.' else 0
    o += str(numpad[r][c])

print(o)
