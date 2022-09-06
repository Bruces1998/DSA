def countPlatforms(n, arr, dep):
    arr.sort()
    dep.sort()

    ans = 1
    count = 1
    arr_index = 1
    dep_index = 0

    while arr_i < n and dep_j < n:
        print(count)
        if arr[arr_i] <= dep[dep_j]:
            count += 1
            arr_i += 1

        else:
            count -= 1
            dep_j += 1
        
        ans = max(ans, count)

    return ans

print(countPlatforms(6, [9, 9.45, 9.55, 11, 15, 18], [9.2, 12, 11.3, 11.5, 19, 20]))