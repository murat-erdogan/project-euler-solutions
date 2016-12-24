import math

def is_prime(num):
    if not num == 1:
        for j in range(2, int(math.sqrt(num)+1)):
            if (num % j) == 0:
                return False
        return True
    else:
        return False


def is_sum_prime(first, second):
    a = str(first) + str(second)
    b = str(second) + str(first)
    if is_prime(int(a)) and is_prime(int(b)):
        return True
    else:
        return False

primes = []
for i in range(3, 1000):
    if is_prime(i):
        primes.append(i)

numbers = []
for k in primes:
    for l in primes:
        if is_sum_prime(k, l):
            numbers.append([k, l])

print(numbers)