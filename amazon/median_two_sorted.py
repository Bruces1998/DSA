def median(num1, num2, m, n):
    if m > n:
        return median(num2, num1, n, m)

    low = 0
    high  = m 
    medianPos = (m+n+1)//2

    while low <= high:
        
        cut1 = (low+high)>>1
        cut2 = medianPos - cut1
        print(cut1, cut2)

        l1 = float("-inf") if cut1 == 0 else num1[cut1-1]
        l2 = float("-inf") if cut2 == 0 else num1[cut2-1]
        r1 = float("inf") if cut1 == m else num1[cut1]
        r2 = float("inf") if cut2 == n else num1[cut2]

        if l1<=r2 and l2<=r1:
            if (m+n)%2 != 0:
                return max(l1, l2)

            else:
                return (max(l1, l2)+min(r1, r2))/2

        elif l1 > l2:
            high = cut1-1
        
        else:
            low = cut1+1

    return 0.0


print(median([1, 4, 7, 10, 12], [2, 3, 6, 15], 5, 4))
