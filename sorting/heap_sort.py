def adjust(a, i, n):
    
    largest = i
    left_child = i*2+1
    right_child = i*2+2

    if left_child < n and a[left_child] > a[largest]:
        largest = left_child

    if right_child < n and a[right_child] > a[largest]:
        largest = right_child

    if i != largest:
        a[i], a[largest] = a[largest], a[i]
        adjust(a, largest, n)



def heapify(arr, n):

    for i in range(n//2 , -1, -1):
        adjust(arr, i, n)
    print(arr)
    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        adjust(arr, 0, i)


    return arr

print(heapify([0, 3, 5, 2, 5, 6, 7, 1], 8))
