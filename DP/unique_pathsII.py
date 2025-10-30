def unique_paths(m, n, grid):
    if grid[0][0] == 1:
        return 0
    
    dp = [[-1]*m]*n

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = 1

            up = 0
            left = 0

            if i > 0:
                up = dp[i - 1][j]

            if j > 0:
                left = dp[i][j - 1]

            if grid[i][j] != 1:
                dp[i][j] = up + left

            else:
                dp[i][j] = 0

    return dp[n - 1][m - 1]

                