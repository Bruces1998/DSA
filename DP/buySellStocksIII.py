'''
Thought behind question:
-> Recursion idea:
    At every index we can do three things:
    1. Buy at that index if nothing to sell and 2 buys not done
    2. Sell at that index if it was bought already and reduce number of buys
    3. Not do anything

    as a result 
    f(ind, buy, cap):
        if ind == n or cap == 0:
            return 0
        if buy == 0:
            profit = max(buy today, do not buy today)

        else:
            profit = max(sell today and reduce cap by 1, do not sell today)

        return profit
'''
def getMaxProfit(arr, n):

    dp = [[[0]*3]*2]*(n+1)

    for ind in range(n-1, -1, -1):
        for buy in range(2):
            for cap in range(1, 3):
                profit =0

                if buy == 0:
                    profit = max(dp[ind+1][1][cap] - arr[ind], dp[ind+1][0][cap])

                else:
                    profit = max(dp[ind+1][0][cap - 1] + arr[ind], dp[ind+1][1][cap])

                dp[ind][buy][cap] = profit

    return dp[0][0][2]

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








