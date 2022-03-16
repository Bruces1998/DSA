def jobScheduling(jobs):
    
    # Write your code here
    # Return an integer denoting the maximum pofit  
    n = len(jobs)
    sorted(jobs, key = lambda x: x[1], reverse = True)
    
    maxx = 0
    for i in range(n):
        maxx = max(maxx, jobs[i][0])
    profit = 0
    
    slots = [0 for _ in range(maxx+1)]
    for i in range(n):
        for j in range(jobs[i][0], 0, -1):
            if slots[j] == 0:
                slots[j] = jobs[i][1]
                profit += jobs[i][1]
                break
                
    return profit