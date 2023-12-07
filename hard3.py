def numberofone(N):
    n=N
    x=1
    count=0
    rem=0
    while n > 0:
        temp = x
        if n % 10 == 0:
            rem = 0
        elif n % 10 > 1:
            rem = temp
        elif n % 10 == 1:
            rem = (N% temp) + 1
        x *= 10 
        count += (N//x) * temp + rem
        n //= 10
    return count
n =int(input())
print(numberofone(n))
