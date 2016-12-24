def calc(numerator, denominator, count, c):
    if count < 997:
        a = (denominator * 2) + numerator
        b = a - denominator
        count += 1
        if len(str(a)) > len(str(b)):
            c += 1
        return calc(a, b, count, c)
    else:
        return c + 1

print(calc(1, 1, 0, 0))