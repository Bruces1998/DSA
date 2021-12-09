def table(n,i):
    if i==0:
        return
    table(n, i-1)
    print(n*i)
table(7, 10)
