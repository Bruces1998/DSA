def backtrack(ans, ds, arr, start):
    ans.append(ds.copy())

    for i in range(start, len(arr)):
        if i > start and arr[i] == arr[i-1]:
            continue
        ds.append(arr[i])
        backtrack(ans, ds, arr, i+1)
        ds.pop(-1)

    
def subsetII():
    ans = []
    ds = []
    inp = list(map(int, input("Array:").split(" ")))
    inp.sort()
    backtrack(ans, ds, inp, 0)
    print(ans)

subsetII()
