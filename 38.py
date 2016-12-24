import itertools
p = list(map("".join, itertools.permutations("123456789")))

for i in range(1000, 9999):
    a = i * 1
    b = i * 2
    if str(a)+str(b) in p:
        print(a, b)