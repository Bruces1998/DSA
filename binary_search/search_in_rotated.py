def search(arr, target):
    if len(arr) <= 1:
        if len(arr) == 1 and arr[0] == target:
            return 0
        return -1

    left = 0
    right = len(arr) - 1
    mid = left + (right -left)//2

    if arr[left] > arr[right]:
        if arr[left] <= arr[mid]:
            while arr[left] <= arr[mid]:
                mid += 1

            if arr[left] <= target <= arr[mid-1]:
                right = mid -1

            else:
                left = mid
        
        else:
            while arr[mid] <= arr[right]:
                mid -= 1
            
            if arr[left] <= target <= arr[mid]:
                right = mid

            else:
                left = mid + 1
    
    while left < right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            return mid
        
        elif arr[mid] <= target:
            left = mid
        
        else:
            right = mid - 1

    if left > right:
        return -1
