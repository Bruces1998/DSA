def missing_repeated_number(arr):
    n = len(arr)+1

    S = n*(n+1)//2
    P = n*(2*n + 1)*(n + 1)//6

    miss = 0
    rep = 0

    for i in range(n-1):
        S -= arr[i]
        P -= arr[i]**2

    miss = (S+P/S)//2
    rep = miss - S 

    return (rep, miss)