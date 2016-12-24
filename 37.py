import math

def is_prime(num):
    if not num == 1:
        for j in range(2, int(math.sqrt(num)+1)):
            if (num % j) == 0:
                return False
        return True
    else:
        return False

def is_truncatable(num):
    i = str(num)
    for j in range(len(i)):
        if is_prime(int(i[j:])):
            continue
        else:
            return False
    for k in range(1, len(i)+1):
        if is_prime(int(i[:k])):
            continue
        else:
            return False
    return True


p = []
for m in range(23, 1000000):
    if is_prime(m):
        p.append(m)

l = []
for i in p:
    if is_truncatable(i):
        l.append(i)
print(sum(l))