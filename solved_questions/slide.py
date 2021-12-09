def maxSum(arr, n, k):
    if not n > k:
        print("Invalid")
        return -1
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
        return max_sum

# Driver code
arr = [3, 1, 0, 20, 0, 2, 1, 4, 2]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
