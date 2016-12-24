j = 1
n = 7830457
for i in range(1, n+1):
    a = str(j*2)
    b = a[-10:]
    j = int(b)

c = str(j*28433+1)
print(c[-10:])
