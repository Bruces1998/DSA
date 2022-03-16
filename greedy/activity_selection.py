def maximumActivities(start, end):
    # Write your Code here.
    n = len(start)
    
    coll = [[start[i], end[i]] for i in range(n)]
    coll.sort(key=lambda x: x[1])
    
    last = coll[0][1]
    ans = 1
    
    for i in range(1, n):
        if coll[i][0] >= last:
            ans += 1
            last = coll[i][1]
            
    return ans