def maxSumSub(arr):

    curr_sum = 0
    max_sum = float("-inf")

    for i in range(0, len(arr)):
        curr_sum = max(curr_sum + arr[i], arr[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

print(maxSumSub([-2,1,-3,4,-1,2,1,-5,4] ))