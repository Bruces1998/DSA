def countPlatforms(n, arr, dep):
    arr.sort()
    dep.sort()

    ans = 1
    count = 1
    i = 1
    j = 0

    while i < n and j < n:
        print(count)
        if arr[i] <= dep[j]:
            count += 1
            i += 1

        else:
            count -= 1
            j += 1
        
        ans = max(ans, count)

    return ans

print(countPlatforms(6, [9, 9.45, 9.55, 11, 15, 18], [9.2, 12, 11.3, 11.5, 19, 20]))