from collections import Counter
lines = open(0).read().strip().splitlines()

column_conut = [Counter(col) for col in zip(*lines)]
count_map = [*map(lambda x: x.most_common(1)[0][0], column_conut)]

gamma = "".join(count_map)
epsilon = "".join(['1' if ch == '0' else '0' for ch in gamma])
print(int(gamma, 2) * int(epsilon, 2))

filtered = []

oxygen = ''
carbon = ''

for line in lines:
           pass