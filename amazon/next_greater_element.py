def next_greater(arr):
    n = len(arr)
    nge = [-1]*n
    stack = []

    for i in range(2*n - 1, -1, -1):
        print(stack)
        while stack and stack[-1] <= arr[i%n]:
            stack.pop(-1)

        if i < n:
            if stack:
                nge[i] = stack[-1]

        stack.append(arr[i%n])

    return nge

print(next_greater([5, 4, 3, 2, 1]))