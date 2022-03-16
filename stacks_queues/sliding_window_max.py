def sliding_window_max(k, arr):
    queue = []
    ans = []
    n = len(arr)

    for i in range(n):
        if queue and queue[0] == i-k:
            queue.pop(0)

        while queue and arr[queue[-1]] < arr[i]:
            queue.pop(-1)

        queue.append(i)
        if i >= i - k:
            ans.append(arr[queue[0]])

    return ans


print(sliding_window_max(3, list(map(int, input("Enter Array:").split(" ")))))