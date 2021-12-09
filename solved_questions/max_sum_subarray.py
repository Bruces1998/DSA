memo = {}
def max_sum(arr, s, e):
    if e < s:
        return 0
    current  = sum(arr[s:e+1])
    if (s, e) not in memo:
        memo[(s, e)] = max(current, max_sum(arr, s+1, e), max_sum(arr, s, e - 1))

    return memo[(s, e)]


print(max_sum([-2, -3, 4, -1, -2, 1, 5, -3], 0, 6))
