def backtrack(ans, ds, arr, start):
    ans.append(ds.copy())

    for i in range(start, len(arr)):
        ds.append(arr[i])
        backtrack(ans, ds, arr, i+1)
        ds.pop(-1)

    
ans = []
ds = []
inp = list(map(int, input("Array:").split(" ")))
backtrack(ans, ds, inp, 0)
print(ans)
