def adjust(a, i, n):
    x = a[i]
    j = i*2

    while(j <= n):
        if j < n and a[j] < a[j+1]:
            j += 1
        
        if x > a[j]:
            break

        a[j//2] = a[j]
        j = j*2

    a[j//2] = x


def heapify(arr, n):

    for i in range(n//2, 0, -1):
        adjust(arr, i, n)

    for i in range(n, 1, -1):
        arr[i], arr[1] = arr[1], arr[i]
        adjust(arr, 1, i-1)


    return arr

print(heapify([0, 3, 5, 2, 5, 6, 7, 1], 7))
