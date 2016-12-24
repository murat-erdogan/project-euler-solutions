import math
def quadratic_primes(a, b):
    c = 0
    for n in range(80):
        num = n*n+a*n+b
        if num > 0 and is_prime(num):
            c += 1
        else:
            return c

def is_prime(num):
    for j in range(2, int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True

m = 0
ll = {}
for k in range(-1000, 1000):
    for l in range(-1000, 1000):
        q = quadratic_primes(k, l)
        if q > m:
            m = q
            ll[m] = k*l
print(ll[m])