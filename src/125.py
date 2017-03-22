palindromes = set()
numbers = set()

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

for i in range(1, 100000000):
    if is_palindrome(i):
        palindromes.add(i)

for i in range(1, 10000):
    s = i**2
    for j in range(i + 1, 10000):
        s += j**2
        if s in palindromes:
            numbers.add(s)

print(sum(numbers))
