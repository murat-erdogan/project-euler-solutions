import math

def is_prime(num):
    for j in range(2, int(math.sqrt(num) + 1)):
        if (num % j) == 0:
            return False
    return True


primes = []
for i in range(2, 100000):
    if is_prime(i):
        primes.append(i)

l = []
for p in primes:
    for n in range(1, 100):
        if pow(10, 10 ** n, 9 * p) == 1:
            l.append(p)
            break

for i in l:
    primes.remove(i)

print(sum(primes))
