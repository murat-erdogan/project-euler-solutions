sum = 0
for i in range(1, 1001):
    sum += i**i
strng = str(sum)
print(strng[-10:])