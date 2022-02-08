def mergeSort(arr, low, high):
    inv = 0
    if low < high:
        mid = (low + high)//2
        inv += mergeSort(arr, low, mid)
        inv += mergeSort(arr, mid+1, high)
        inv += merge(arr, low, mid, high)

    return inv


def merge(arr, low, mid, high):

    total = 0
    j = mid+1
    for i in range(low, mid+1):
        while(j <= high and arr[i] > 2*arr[j]):
            j += 1

        total += (j - (mid+1))

    
    i = low
    j = mid+ 1
    t = []

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            t.append(arr[i])
            i += 1

        else:
            t.append(arr[j])
            j += 1
    
    if i > mid:
        while(j <= high):
            t.append(arr[j])
            j += 1
    
    else:
        while(i <= low):
            t.append(arr[i])
            i += 1

    for i in range(low, high+1):
        arr[i] = t[i-low]

    return total
