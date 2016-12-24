import math
import itertools
primes = []

def is_prime(num):
    for j in range(2, int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True

for i in range(1000, 9999):
    if is_prime(i):
        primes.append(i)

for j in primes:
    l = list(map("".join, itertools.permutations(str(j))))
    a = j + 3330
    b = j + 6660
    if str(a) in l and str(b) in l and a in primes and b in primes:
        print(str(j) + str(a) + str(b))