def pentagonal(n):
    return n*(3*n-1)//2

def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return True
    return False

p = []
ps = []
for i in range(1, 5000):
    p.append(pentagonal(i))

for j in p:
    for k in p:
        if binary_search(p, j+k) and binary_search(p, k-j):
            print(j-k)

