def trap(heights):
    n = len(heights)
    
    #base case
    if n <= 2:
        return 0
    
    ans = 0 #to store the answer
    k = 0 #iterator

    while k != n:
        i = k + 1 #inner iter
        last_max = i

        while i < n and heights[k] > heights[i]:
            if heights[i] >= heights[last_max]:
                last_max = i
            i += 1

        if i == k + 1:
            k += 1
            continue

        if  i == n:
            i = last_max

        dist = i - k - 1
        if dist > 0:
            area = dist*min(heights[i], heights[k])
            k += 1

            while k != i:
                area -= heights[k]
                k += 1

            ans += area

        else:
            k += 1

    return ans


print(trap(list(map(int, input("Enter Heights:").split(" ")))))