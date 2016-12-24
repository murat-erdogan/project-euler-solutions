l = []
for i in range(1, 10):
    for j in range(1, 10):
        a = str(i**j)
        if int(a) == int(a[-1:])**j:
            l.append(a)

print(len(l))