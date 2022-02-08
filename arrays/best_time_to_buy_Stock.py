def maxProfit(arr):
    maxx = 0
    minn = float("inf")

    for i in range(len(prices)):
        if prices[i]< minn:
            minn = prices[i]

        elif prices[i] - minn > maxx:
            maxx = prices[i] - minn

    return maxx