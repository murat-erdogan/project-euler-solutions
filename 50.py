# I started brute forcing and did not wait it to finish.
# after 2-3 mins i stopped it and took the list.
# then sorted the list by first value and second value is the result.
import math
primes = []

def is_prime(num):
    for j in range(2, int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True

for i in range(2, 1000000):
    if is_prime(i):
        primes.append(i)

s = 0
for j in range(len(primes)-1):
    for k in range(len(primes)-j):
        s += primes[k+j]
        if s < 1000000 and s in primes:
            print(len(primes[j: k+j+1]), s)
    s = 0