l = []
for i in range(10, 99):
    for j in range(10, 99):
        if i/j < 1:
            a = str(i)
            b = str(j)
            if not j % 10 == 0 and not i % 10 == 0:
                if i/j == int(a[0])/int(b[0]):
                    if a[1] == b[1]:
                        l.append(i/j)
                if i/j == int(a[0])/int(b[1]):
                    if a[1] == b[0]:
                        l.append(i/j)
                if i/j == int(a[1])/int(b[0]):
                    if a[0] == b[1]:
                        l.append(i/j)
                if i/j == int(a[1])/int(b[1]):
                    if a[0] == b[0]:
                        l.append(i/j)
print(l)
"""
16/64 = 1/4
19/95 = 1/5
26/65 = 2/5
49/98 = 1/2
"""