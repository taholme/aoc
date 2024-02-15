cache = {}


def count(springs, conditions):
    if springs == "":
        return 1 if conditions == () else 0
    if conditions == ():
        return 0 if "#" in springs else 1

    key = (springs, conditions)
    if key in cache:
        return cache[key]

    result = 0
    if springs[0] in ".?":
        result += count(springs[1:], conditions)
    if springs[0] in "#?" and (
                conditions[0] <= len(springs)
                and "." not in springs[: conditions[0]]
                and (conditions[0] == len(springs) or springs[conditions[0]] != "#")
            ):
        result += count(springs[conditions[0] + 1 :], conditions[1:])

    cache[key] = result
    return result


t = 0

for line in open(0):
    springs, conditions = line.split()
    conditions = tuple(map(int, conditions.split(",")))

    springs = "?".join([springs] * 5)
    conditions *= 5

    t += count(springs, conditions)

print(t)
