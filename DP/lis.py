'''
Thought behind the question:
-> Recursion idea:
    At any index after 0, we can do following:
    1. If it is greater than previous, consider it
    2. Do not consider it
    
    As a result
    f(ind, prev):
        if ind == n:
            return 0
        
        notTake = 0 + f(ind+1, prev)
        take = 0

        if prev == -1 or arr[ind] > arr[prev]:
            take = 1 + f(ind + 1, ind)

        return max(take, notTake)
            
'''

def LIS(nums):
    n = len(nums)
    dp = [[0]*(n+1)]*(n+1)

    for ind in range(n-1, -1, -1):
        for prev in range(ind - 1, -2, -1):
            notTake = 0 + dp[ind + 1][prev + 1]
            take = 0

            if nums[ind] > nums[prev] or prev == -1:
                take = 1 + dp[ind + 1][ind+1]

            dp[ind][prev + 1] = max(notTake, take)


    return dp[0][0]


##Optimised solution

def LIS(arr, n):
    dp = [1]*n
    mapp = {}
    lastIndex = -1
    ans = -1

    for ind in range(n):
        mapp[ind] = ind
        for prev in range(ind):

            if arr[ind] > arr[prev] and dp[ind] < 1 + dp[prev]:
                dp[ind] = 1 + dp[prev]
                mapp[ind] = prev


        if dp[ind] > ans:
            ans = dp[ind]
            lastIndex = ind

    
    ans_arr = [arr[lastIndex]]

    while mapp[lastIndex] != lastIndex:
        lastIndex = mapp[lastIndex]
        ans_arr.append(arr[lastIndex])

    return ans_arr[::-1]


    

nums = [4,10,4,3,8,9]

print(LIS(nums, 6))