import itertools
c = list(map("".join, itertools.permutations('0123456789')))
d = 0
c.sort()

for i in c:
    d += 1
    if d == 1000000:
        print(i)
        break
