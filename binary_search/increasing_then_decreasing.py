def binarySearch(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = left + (right - left)//2

        if right == left + 1:
            if arr[left] >= arr[right]:
                return arr[left]
            
            else:
                return arr[right]
        
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return arr[mid]

        if arr[mid] < arr[mid-1] and arr[mid] > arr[mid+1]:
            right = mid - 1

        else:
            left = mid + 1

    return -1



print(binarySearch([8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]))

        

        