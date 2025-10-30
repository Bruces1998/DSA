'''
The idea behind this question is that around the peak element,
the element to the left side are on an incrasing trend till the 
peak and from there they are on a decreasing trend till the
right so the best way to know which part of the array you are 
in to find this trend.
'''
def findPeakElement( arr: List[int]) -> int:
    n = len(arr)
    if n == 1:
        return 0
    
    if arr[0] > arr[1]:
        return 0
    
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    low = 1
    high = n - 2

    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        
        elif arr[mid] > arr[mid - 1]:
            low = mid + 1
        
        else:
            high = mid - 1
    
    return -1