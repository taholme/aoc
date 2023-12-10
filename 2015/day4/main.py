from hashlib import md5

inp = open(0).read().strip()


def findHash(zeros):
    found = False
    i = 0
    while not found:
        i += 1
        md5hash = md5((inp + str(i)).encode("utf-8")).hexdigest()
        if "0" * zeros == md5hash[:zeros]:
            print(f"{i=}, {md5hash=}")
            found = True


findHash(5)
findHash(6)
