'''
Intuition:
    We have strings S1 and S2 with i and j index
    At any index i for S1 we can do the following:
    1. if S1[i] == S2[j], continue for i-1, j-1
    2. if insert, we call i, j - 1 -> inserting in S1 and then coming back in S2 by 1
    3. if delete, we call i - 1, j -> deleting in S1 so coming back in S1 by 1
    4. if replace, we call i - 1, j - 1 -> replacing in S1 and hence it becomes similar to case 1
'''
def editDistance(S1, S2):
    n = len(S1)
    m = len(S2)

    def edUtil(i, j):
        if i < 0:
            return j + 1
        
        if j < 0:
            return i + 1
        
        if S1[i] == S2[j]:
            return edUtil(i-1, j-1)
        
        else:
            return 1 + min(edUtil(i-1, j-1), min(edUtil(i-1, j), edUtil(i, j-1)))
        
    return edUtil(n - 1, m - 1)


def editDistanceDP(S1, S2):

    n = len(S1)
    m = len(S2)

    dp = [[0]*m+1]*n+1

    for i in range(n):
        dp[i][0] = i

    for j in range(m):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):

            if S1[i-1] == S2[j-1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])


    return dp[n][m]


### Space Optimized Approcach ###
def editDistanceDP(S1, S2):

    n = len(S1)
    m = len(S2)

    prev = [j for j in range(m)]
    curr = [0 for j in range(m)]

    for i in range(1, n+1):
        curr[0] = i
        for j in range(1, m+1):

            if S1[i-1] == S2[j-1]:
                curr[j] = prev[j - 1]

            else:
                curr[j] = min(prev[j], curr[j-1], prev[j-1])

        prev, curr = curr, prev
    return curr[m]

