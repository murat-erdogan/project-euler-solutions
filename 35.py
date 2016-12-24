import math
def is_circular_prime(n):
    a = str(n)
    for i in range(len(a)):
        d = a[i:] + a[:i]
        if not is_prime(int(d)):
            return False
    return True


def is_prime(num):
    for j in range(2, int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True

count = 0
for k in range(2, 1000000):
    if is_prime(k):
        if is_circular_prime(k):
            count += 1

print(count)