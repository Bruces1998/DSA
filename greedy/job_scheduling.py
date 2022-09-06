def jobScheduling(jobs):
    
    # Write your code here
    # Return an integer denoting the maximum pofit  
    n = len(jobs)
    jobs = sorted(jobs, key = lambda x: x[2], reverse = True)
    
    print(jobs)
    maxx = 0
    for i in range(n):
        maxx = max(maxx, jobs[i][1])
    profit = 0
    
    slots = [-1 for _ in range(maxx+1)]
    for i in range(n):
        for j in range(jobs[i][1], 0, -1):
            if slots[j] == -1:
                slots[j] = i
                profit += jobs[i][2]
                break
                
    return profit


jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
N = 4
print(jobScheduling(jobs))