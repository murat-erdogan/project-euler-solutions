import math

f = open('p099_base_exp.txt', 'r')
l = []
for line in f:
    b = str(line)
    c = b.split(',')
    a = 1 + float(c[1]) * math.log(float(c[0]), 10)
    l.append(a)
    print(b, a)
print("-", max(l))