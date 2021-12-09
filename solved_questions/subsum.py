memo = {}
def subsum(arr,n, x):
    if x==0:
        return True
    if n==0:
        return False
    if arr not in memo:

        if int(arr[0]) > x:
            memo[arr] = subsum(arr[1:], n - 1, x)

        memo[arr] = (subsum(arr[1:], n - 1, x) or subsum(arr[1:], n - 1, x - int(arr[0])))

    return memo[arr]

print(subsum("327234561", 4, 13))
