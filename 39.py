import math
from collections import defaultdict

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False

s = []
for i in range(1, 1000000):
    if is_square(i):
        s.append(i)

sm = defaultdict(int)
for m in range(1, 1001):
    for n in range(1, 1001):
        a = m**2 + n**2
        if a in s:
            c = m+n+int(math.sqrt(a))
            if c <= 1000:
                sm[c] += 1

mx = 0
nx = 0
for jk in sm:
    if sm[jk] > mx:
        mx = sm[jk]
        nx = jk
print(mx, nx)