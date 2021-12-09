def knap(pw, m, n, memo):
    if m==0:
        return
    knap(pw, m-1,n, memo)
    
    for i in range(1, n+1):
        if m >=pw['weights'][i-1]:
            memo[i][m] = max( memo[i-1][m], pw['profits'][i-1] + memo[i - 1][m - pw['weights'][i-1]])
            
        else:
            memo[i][m] = memo[i - 1][m]
            
            
    return


profit_weights = {'profits':[12, 10, 20, 25],'weights':[2, 1, 3, 2]}
import numpy as np
memo = np.zeros((5,6))
knap(profit_weights, 5, 4, memo)
print(memo)