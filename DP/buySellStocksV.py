'''
Thought behind question:
-> Recursion idea:
    At every index we can do three things:
    1. Buy at that index if nothing else was bought already
    2. Sell at that index if it was bought already and add fee
    3. Do nothing

    as a result 
    f(ind, buy):
        if buy == 0:
            profit = max(buy today, do not buy today)

        else:
            profit = max(sell today with fee, do not sell today)

        return profit
'''

def getMaxProfit(arr, n, fee):

    dp = [[-1]*2]*(n+1)
    print(dp)
    dp[n][1] = dp[n][0] =  0
    

    for ind in range(n-1, -1, -1):
        for buy in range(2):
            profit =0

            if buy == 0:
                profit = max(dp[ind+1][1] - arr[ind], dp[ind+1][0])

            else:
                profit = max(dp[ind+1][0] + arr[ind] - fee, dp[ind+1][1])

            dp[ind][buy] = profit

    return dp[0][0]

prices = [1,3,7,5,10,3]
fee = 3
print(getMaxProfit(prices, 6, fee))