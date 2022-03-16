def trap(height) -> int:
    n = len(height)
    if n <= 2:
        return 0
    
    k = 0
    ans = 0
    while k != n:

        i = k + 1
        last_max = i

        while(i < n and height[k] > height[i]):
            if height[i] >= height[last_max]:
                last_max = i
            i += 1

        if i == k + 1:
            k += 1
            continue
        
        if i == n:
            i = last_max
                
        dist = i - k - 1
        # print(k, i, dist)
        
        if dist > 0:
            
            area = dist*min(height[k], height[i])
            # print(area)
            k += 1
            while(k != i):
                area -= height[k]
                k+=1
                
                
                
            ans += area
            
        else:
            k += 1
            

    return ans

height = list(map(int, input("Enter Height:").split(" ")))
print(trap(height))