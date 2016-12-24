max = 0
for i in range(100):
    for j in range(100):
        a = ""
        a = str(i**j)
        sum = 0
        for k in a:
            sum += int(k)
        if sum > max:
            max = sum
print(max)