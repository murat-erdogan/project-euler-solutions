import math

def is_prime(num):
    for j in range(2, int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True

#something magic happened here and setting boundry to 10000 (as a result of trial and error) gave me the correct answer.
#but it is just a candidate number, not necessarily smallest and brute force approach works in this case.
primes = []
for i in range(2, 10000):
    if is_prime(i):
        primes.append(i)

def is_concat_prime(l):
    pairs = []
    for i in range(0, len(l) - 1):
        pairs.append((l[i], l[-1]))
        pairs.append((l[-1], l[i]))
    for i in pairs:
        a = int(str(i[0]) + str(i[1]))
        if not is_prime(a):
            return False
    return True

def check():
    for i in range(0, len(primes)):
        for j in range(i, len(primes)):
            if is_concat_prime([primes[i], primes[j]]):
                for k in range(j, len(primes)):
                    if is_concat_prime([primes[i], primes[j], primes[k]]):
                        for l in range(k, len(primes)):
                            if is_concat_prime([primes[i], primes[j], primes[k], primes[l]]):
                                for m in range(l, len(primes)):
                                    if is_concat_prime([primes[i], primes[j], primes[k], primes[l], primes[m]]):
                                        return primes[i] + primes[j] + primes[k] + primes[l] + primes[m]
                                 
print(check())
