"""
About Heap:
Two types:
1. Min Heap: smallest element at the top
2. Max Heap: largest element at the top

Major operations:
1. Insert: Insert an element in the heap in O(logN) time
2. Delete: Delete the root in the heap in O(1) time
3. Heapify: Convert an array into heap
"""
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

    for i in range((n//2), -1, -1):
        adjust(arr, i, n)
    print(arr)
    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        adjust(arr, 0, i)


    return arr

print(heapify([0, 3, 5, 2, 5, 6, 7, 1], 8))
