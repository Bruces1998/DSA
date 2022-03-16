def backtrack(arr, target, ans, ds, start):
    if target < 0:
        return 
    if target == 0:
        ans.append(ds.copy())

    else:
        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i-1]:
                continue
            ds.append(arr[i])
            backtrack(arr, target-arr[i], ans, ds, i+1)
            ds.pop(-1)
def solve(arr, target):
    ans = []
    ds = []
    arr.sort()
    backtrack(arr, target, ans, ds, 0)

    return ans

if __name__ == "__main__":
    inp = list(map(int, input("Array:").split(" ")))
    target = int(input("target: "))
    print(solve(inp, target))
