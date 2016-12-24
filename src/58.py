import math


def is_prime(num):
    for j in range(2, int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True

l = []
nl = []
j = 1
for i in range(1, 15000):
    a = j + 2 * i
    b = a + 2 * i
    c = b + 2 * i
    d = c + 2 * i
    j = d
    n = i * 2 + 1
    if is_prime(a):
        l.append(a)
    else:
        nl.append(a)
    if is_prime(b):
        l.append(b)
    else:
        nl.append(b)
    if is_prime(c):
        l.append(c)
    else:
        nl.append(c)
    if is_prime(d):
        l.append(d)
    else:
        nl.append(d)

    x = len(l)
    y = len(nl) + len(l) + 1
    ratio = x/y * 100
    #print(a, b, c, d, n, x, y, ratio)
    if ratio < 10:
        print(n)
        break