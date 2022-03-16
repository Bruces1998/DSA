def backtrack(ans, ds, arr, start, target):
    if target < 0:
        return

    if target == 0:
        ans.append(ds.copy())

    else:
        for i in range(start, len(arr)):
            ds.append(arr[i])
            backtrack(ans, ds, arr, i, target-arr[i])
            ds.pop(-1)

def solve(arr, target):
    ans = []
    ds = []

    backtrack(ans, ds, arr, 0, target)
    return ans

if __name__ == "__main__":
    inp = list(map(int, input("Array:").split(" ")))
    target = int(input("target: "))
    print(solve(inp, target))