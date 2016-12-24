count = 1
sum = 0
for i in range(1, 501):
    for j in range(4):
        count += 2*i
        sum += count
print(sum+1)