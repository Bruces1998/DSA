def countWays(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    if n ==2:return 2
    a = 1
    b = 2
    for i in range(2,n):
        c = a+b
        a = b
        b = c

    return c

print(countWays(21))
