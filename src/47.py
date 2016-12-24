# this cheesy code can calculate in 1-2 mins
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    list2 = sorted(set(factors),key=factors.index)
    return list2

l = {}
for i in range(2, 1000000):
    a = prime_factors(i)
    if len(a) == 4 and a[0] != a[1] and a[1] != a[2] and a[0] != a[2] and a[0] != a[3] and a[1] != a[3] and a[2] != a[3]:
        l[i] = 1
    else:
        l[i] = 0

for j in range(2, len(l)):
    if l[j] == 1 and l[j+1] == 1 and l[j+2] == 1 and l[j+3] == 1:
        print(j, j+1, j+2, j+3)
        break