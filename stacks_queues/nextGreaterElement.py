def nextGreater(nums):
    n = len(nums)
    nge = [-1]*n
    stack = []
    for i in range(2*n-1, -1, -1):
        while stack and stack[-1] <= nums[i%n]:
            stack.pop(-1)

        if i < n:
            if stack:
                nge[i] = stack.pop(-1)
        stack.append(nums[i%n])

    return nge

print(nextGreater([5, 7, 1, 2, 6, 0]))