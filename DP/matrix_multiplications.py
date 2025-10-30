'''
Matrix multiplication Happens between 
1. A1[p x q] and A2[r x s] if q == r
2. Total calculations = p x q x s

'''

def mat_multi(arr):
    dp = [[-1]*len(arr)]*len(arr)

    start = 1
    end = len(arr) - 1

    def chain_multiply(arr, start, end):
        if start == end:
            return 0
        
        if dp[start][end] == -1:
            for k in range(start, end):
                count = chain_multiply(arr, start, k) + arr[start - 1] * arr[k] * arr[end] * chain_multiply(arr, k+1, end)

                dp[start][end] = min(dp[start][end], count)


        return dp[start][end]
    
    return chain_multiply(arr, start, end)