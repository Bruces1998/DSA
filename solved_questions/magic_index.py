def magic_bin(arr, start, end):
    if end < start:
        return -1

    mid = (start + end) // 2
    midval = arr[mid]
    if mid == midval:
        return mid

    leftind = min(midval, mid - 1)
    left = magic_bin(arr, start, leftind)
    if left >=0:
        return left

    rightind = max(midval, mid + 1)
    right = magic_bin(arr, rightind, end)
    return right


if __name__ == "__main__":
    arr = [-40, -5, 0, 1, 4, 4, 4, 7, 9, 12, 13]
    a = magic_bin(arr, 0,len(arr) )
    print(a)
