fraction = ""
for n in range(1, 200000):
    fraction += str(n)

print(int(fraction[0]) * int(fraction[9]) * int(fraction[99]) * int(fraction[999]) \
      * int(fraction[9999]) * int(fraction[99999]) * int(fraction[999999]))