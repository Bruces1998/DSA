def swap(a, b):
    a, b = b, a
    return 
def sortColors(arr):
    start = 0
    end = len(arr) - 1
    mid = 0

    while(mid <= end):
        if arr[mid] == 0:
            swap(arr[mid], arr[start])
            start += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        else:
            swap(arr[mid], arr[end])
            end -= 1