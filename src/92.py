def square_digit(n):
    s = 0
    while n:
        s += (n % 10) ** 2
        n //= 10
    if s == 1 or s == 89:
        return s
    else:
        return square_digit(s)

c = 0
for i in range(1, 10000000):
    if square_digit(i) == 89:
        c += 1
print(c)