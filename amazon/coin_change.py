def getCoins(S, m, n):

    table = [0 for k in range(n+1)]

    table[0] = 1

    for i in range(0, m):
        for j in range(S[i], n+1):
            print(table)
            table[j] += table[j-S[i]]


    return table[n]

arr = [1, 2, 3]
m = len(arr)
n = 4

print(getCoins(arr, m, n))