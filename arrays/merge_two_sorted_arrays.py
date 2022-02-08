'''
Merge two sorted arrays
without extra space.
'''
def merge(arr1, arr2):
    
    for i in range(len(arr1)):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
        

        first = arr2[0]

        k = 1
        while(k < len(arr2) and arr2[k] < first):
            arr2[k-1] = arr2[k]
            k += 1

        arr2[k-1] = first


    return (arr1, arr2)


'''
Merge both the arrays in the extra 
space provided in array 1.
'''
def merge_2(nums1, nums2, m, n):
    total_length = m+n-1
    i = m-1
    j = n-1

    while(j > -1 and i > -1):
        if nums1[i] > nums2[j]:
            nums1[total_length] = nums1[i]
            i -= 1
            total_length -= 1

        else:
            nums1[total_length] = nums2[j]
            total_length -= 1
            j -= 1

    if i == -1:
        for ele in range(j, -1, -1):
            nums1[total_length] = nums2[ele]
            total_length -= 1
    else:
        for ele in range(i, -1, -1):
            nums1[total_length] = nums1[ele]
            total_length -= 1

    return nums1