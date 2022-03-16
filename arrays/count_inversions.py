def merge(arr, left, mid, right, inv_count):
    # inv_count = 0
    temp = [0]*10
    i = left
    j = mid
    k = -1

    while i <= mid-1 and j <=right:
        if arr[i] <= arr[j]:
            k +=1
            temp[k] = arr[i]
            i+=1

        else:
            k+=1
            temp[k] = arr[j]
            inv_count.append((i, j))
            j+=1

    if i == mid:
        for w in range(j, right+1):
            k += 1
            temp[k] = arr[w]

    else:
        for w in range(i, mid):
            k += 1
            temp[k] = arr[w]

    for w in range(k+1):
        arr[left+w] = temp[w]


def mergeSort(arr, left, right, ans):
    mid = (left+right)//2
    if left < right:
        mergeSort(arr, left, mid, ans)
        mergeSort(arr, mid+1, right, ans)

        merge(arr, left, mid+1, right, ans)


ans = []
print(mergeSort([5, 3, 2, 1, 4], 0, 4,ans ))
print(ans)