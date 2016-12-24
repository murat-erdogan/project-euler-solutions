import math

def c(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

l = []
for i in range(2, 101):
    for j in range(1, i):
        a = c(i, j)
        if a > 1000000:
            l.append(a)

print(len(l))