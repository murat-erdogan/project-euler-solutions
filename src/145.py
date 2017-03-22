def is_reversible(n):
    a = str(n)[::-1]
    b = str(int(a) + n)
    for j in range(0, ((len(b))//2)+1):
        if not int(b[j]) % 2:
            return False
    return True

c = 0
for i in range(10, 1000000000):
    if i % 10:
        if is_reversible(i):
            c += 1
print(c)
