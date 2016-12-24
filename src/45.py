def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return True
    return False

t = []
p = []
h = []
for n in range(2, 1000000):
    t.append(n*(n+1)//2)
    p.append(n*(3*n-1)//2)
    h.append(n*(2*n-1))

for i in t:
    if binary_search(p, i):
        if binary_search(h, i):
            print(i)