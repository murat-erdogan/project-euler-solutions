def triangular(n):
    sum_ = 0
    for i in range(n+1):
        sum_+= i
    return sum_


def divisors(n):
    count=2
    i=2
    while(i**2 <= n):
        if(n%i==0):
            count+=2
        i+=1
    return count

for i in range(100000):
    tn = triangular(i)
    dtn = divisors(tn)
    if dtn > 500:
        print(i)