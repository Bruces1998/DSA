def majority_ele(arr):
    n = len(arr)
    cnt = 0
    ele = None

    for i in range(n):
        if cnt == 0:
            ele = arr[i]
            cnt += 1

        elif arr[i] != ele:
            cnt -= 1
        
        else:
            cnt += 1

    cnt = 0
    for i in range(n):
        if arr[i] == ele:
            cnt += 1

    if cnt > n//2:
        return cnt
    
    return -1
    