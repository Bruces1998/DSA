'''
Thought behind question:
-> Recursion idea:
    At every index we can do three things:
    1. Buy at that index if nothing else was bought already
    2. Sell at that index if it was bought already
    3. Do nothing

    as a result 
    f(ind, buy):
        if ind == n:
            return 0
        if buy == 0:
            profit = max(buy today, do not buy today)

        else:
            profit = max(sell today, do not sell today)

        return profit
'''
def getMaxProfit(arr, n):

    dp = [[-1]*2]*(n+1)
    dp[n][0] = dp[n][1] = 0

    for ind in range(n-1, -1, -1):
        for buy in range(2):
            profit =0

            if buy == 0:
                profit = max(dp[ind+1][1] - arr[ind], dp[ind+1][0])

            else:
                profit = max(dp[ind+1][0] + arr[ind], dp[ind+1][1])

            dp[ind][buy] = profit

    return dp[0][0]

###Space Optimized ###
def getMaxProfit(arr, n):
    ahead = [0, 0]  # Initialize two lists, 'ahead' and 'cur', to keep track of profits for buying and selling
    cur = [0, 0]
    
    # Base condition: Initialize both 'ahead' and 'cur' to 0, as there are no more days to trade
    ahead[0] = ahead[1] = 0
    
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            profit = 0
            
            if buy == 0:
                # We can buy the stock
                profit = max(0 + ahead[0], -arr[ind] + ahead[1])
            elif buy == 1:
                # We can sell the stock
                profit = max(0 + ahead[1], arr[ind] + ahead[0])
            cur[buy] = profit  # Store the result in the 'cur' list
        
        ahead = cur  # Update 'ahead' to be the same as 'cur'
    
    return cur[0]








