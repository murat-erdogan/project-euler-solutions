import itertools
import math
primes = []

# try 123456789, 12345678, 1234567 in decreasing order and bump!
l = list(map("".join, itertools.permutations("1234567")))

def is_prime(num):
    for j in range(2, int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True

m = 0
for i in l:
    if is_prime(int(i)):
        m = i

print(m)