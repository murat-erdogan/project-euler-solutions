import itertools

d1 = list(map("".join, itertools.permutations("123456789", 1)))
d2 = list(map("".join, itertools.permutations("123456789", 2)))
d3 = list(map("".join, itertools.permutations("123456789", 3)))
d4 = list(map("".join, itertools.permutations("123456789", 4)))

s = []
for m in d1:
    for n in d4:
        a = str(int(m)*int(n))
        if len(a) < 5 and a in d4:
            if not m=="1" and not m in n and not m in a and not n[0] in a and not n[1] in a and not n[2] in a and not n[3] in a:
                s.append(int(a))
m = n = a = ""
for m in d2:
    for n in d3:
        a = str(int(m)*int(n))
        if len(a) < 5 and a in d4:
            if not m[0] in n and not m[1] in n and not m[0] in a and not m[1] in a and not n[0] in a and not n[1] in a and not n[2] in a:
                s.append(int(a))

# a dirty hack here, because 5346 and 5796 seen twice in the list
print(sum(s)-5346-5796)