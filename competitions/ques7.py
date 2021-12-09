from itertools import combinations
def get_expansion(n, string):
    strings = list(combinations(range(n+1), 2))
    m = len(strings)
    if m==1:
        return 1
    
    dp = [1]*m
    maxx = dp[0]
    for i in range(m-1):
        for j in range(i+1, m):
            if string[strings[j][0]:strings[j][1]] > string[strings[i][0]:strings[i][1]]:
                dp[j] = max(dp[j], 1+dp[i])
                maxx = max(maxx, dp[j])
                
    return maxx

n = int(input())
inp = []
n_inp = []
for i in range(n):
    n_inp.append(int(input()))
    inp.append(input())
    
for i in range(n):
    print(get_expansion(n_inp[i], inp[i]))
