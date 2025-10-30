def subsetSum(arr, K):
    n = len(arr)

    dp = [[-1]*(K+1)]*n

    for i in range(n):
        dp[i][0] = True

    for j in range(1, K+1):

        if arr[0] == j:
            dp[0][j] = True

    
    for i in range(1, n):
        for j in range(1, K+1):
            a1 = dp[i - 1][j]
            if arr[i] <= K:
                a1 = dp[i - 1][j - arr[i]] or a1

            dp[i][j] = a1

    return dp[n - 1][K]

arr = [1, 2, 3, 4]
K = 4
print(subsetSum(arr, K))