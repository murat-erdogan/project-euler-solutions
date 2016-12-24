def is_palindrome(n):
    a = str(n)
    b = len(a)

    if b % 2 == 0:
        c = a[:b//2]
        d = a[b//2:]
        if d[::-1] == c:
            return True
        else:
            return False
    else:
        e = a[:b//2]
        f = a[(b//2)+1:]
        if f[::-1] == e:
            return True
        else:
            return False

palindrome_ten = []
for j in range(10):
    palindrome_ten.append(j)

for i in range(10, 1000000):
    if is_palindrome(i):
        palindrome_ten.append(i)

s = 0
for k in palindrome_ten:
    g = "{0:b}".format(k)
    if is_palindrome(g):
        s += k

print(s)