def permutations(arr):

    def backtrack(arr, ans, ds):
        if len(ds) == len(arr):
            ans.append(ds.copy())
            return

        for i in range(len(arr)):
            if arr[i] not in ds:
                ds.append(arr[i])
                backtrack(arr, ans, ds)
                ds.pop(-1)

    ans = []
    ds = []
    backtrack(arr, ans, ds)
    return ans

# inp = list(map(int, input("Array:").split(" ")))
print(permutations(input().split(" ")))
