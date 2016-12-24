import math
result = 0
for i in range(3, 1000000):
    a = str(i)
    sum = 0
    for j in range(len(a)):
        sum += math.factorial(int(a[j]))
    if sum == i:
        result += sum

print(result)