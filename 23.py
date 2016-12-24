import math
abundants = []
limit = 28123

def divisors(n):
    yield 1
    largest = int(math.sqrt(n))
    if largest * largest == n:
        yield largest
    else:
        largest += 1
    for i in range(2, largest):
        if n % i == 0:
            yield i
            yield n / i

for i in range(12, limit):
    if sum(divisors(i)) > i:
        abundants.append(i)

nums = {}
for y in range(limit+1):
    nums[y] = 0

a = 0
for k in range(len(abundants)):
    for m in range(k, len(abundants)):
        a = abundants[k] + abundants[m]
        if a < limit:
            nums[a] = 1
        else:
            break
s = 0
for y in range(limit):
    if nums[y] == 0:
        s += y
print(s)