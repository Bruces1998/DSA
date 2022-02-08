def maxSumSub(arr):

    curr_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        curr_sum += arr[i]
        if curr_sum < 0:
            curr_sum = 0

        max_sum = max(max_sum, curr_sum)

    return max(max_sum, max(arr))