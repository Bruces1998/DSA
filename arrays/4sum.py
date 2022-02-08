def fourSum(arr, target):
    n = len(arr)
    if n < 4:
        return []
    
    arr.sort()

    for i in range(n-3):
        for j in range(n-2):
            val = target - (arr[i] + arr[j])
            low = j + 1
            high = n - 1

            while(low < high):
                if val < arr[low] + arr[high]:
                    high -= 1
                
                elif val > arr[low] + arr[high]:
                    low -= 1

                else:
                    return [arr[x] for x in (i, j, low, high)]

    return []
