def minCoinsGreedy(coins, V):
    coins.sort()
    ans = 0

    for i in range(len(coins)-1, -1, -1):

        while V >= coins[i]:
            V -= coins[i]
            ans += 1


    return ans
