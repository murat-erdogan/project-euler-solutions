def palindrome(n, count):
    if count < 50:
        a = str(n)
        b = a[::-1]
        c = n + int(b)
        d = str(c)
        count += 1
        if not d[::-1] == d:
            return palindrome(c, count)
        else:
            return 1
    else:
        return 0

cnt = 0
for i in range(10000):
    if not palindrome(i, 0):
        cnt += 1

print(cnt)