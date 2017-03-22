import math


def is_prime(num):
    for j in range(2, int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True

primes = []
for i in range(2, 200000):
    if is_prime(i):
        primes.append(i)

c = 0
sum = 0
for p in primes:
    if(pow(10, 1000000000, 9*p) == 1):
        c += 1
        if(c > 40):
            break
        sum += p

print(sum)
