nums = []

for i in range(2, 101):
    for j in range(2, 101):
        a = i**j
        nums.append(a)

s = []
for k in nums:
    if k not in s:
        s.append(k)

s.sort()
count = 0
for m in s:
    count += 1
print(count)
