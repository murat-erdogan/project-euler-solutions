import itertools
def is_permuted(n):
    a = str(n)
    c = list(map("".join, itertools.permutations(a)))
    if str(n*2) not in c:
        return False
    if str(n*3) not in c:
        return False
    if str(n*4) not in c:
        return False
    if str(n*5) not in c:
        return False
    if str(n*6) not in c:
        return False
    return True

for i in range(1, 150000):
    if is_permuted(i):
        print(i)