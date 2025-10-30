from pprint import pprint
'''
Thoughts:
    Here for every index of pattern we have following choices:
    1. The ith character matches the given string. Hence we 
    call f(i - 1, j - 1)
    2. The ith character is ?, hence we treat it as a match and 
    call f(i - 1, j - 1)
    3. The ith chracter is *, hence we have following two cases
    a. Consider * matching with nothing -> f(i - 1, j)
    b. Consider * matching with just current -> f(i - 1, j - 1)
    c. Consider * matching with current and keeping it -> f(i, j - 1)

    Now here the second automatically gets covered using the first case
    e.g. f(i, j) -> f(i - 1, j) -> f(i - 1, j - 1)
'''

def wildcard_matching(p, s):

    def wmUtil(i, j):

        if i < 0 and j < 0:
            return True

        if j < 0 and i >= 0:
            return p[i] == "*"

        if i > 0 or j < 0:
            return False
        
        if p[i] == s[j]:
            return wmUtil(i - 1, j - 1)
        
        else:
            if p[i] == "?":
                return wmUtil(i - 1, j - 1)
            
            elif p[i] == "*":
                return wmUtil(i, j - 1) or wmUtil(i - 1, j)
            
            else:
                return False    
            
    n = len(p)
    m = len(s)

    return wmUtil(n - 1, m - 1)

def wildcard_matching(p, s):
    n = len(p)
    m = len(s)

    dp = [[False]*(m+1)]*(n+1)

    

    for i in range(1, n+1):
        print(p[i-1], dp[i][0])
        dp[i][0] = (p[i-1] == "*")
        pprint(dp)

    dp[0][0] = True


    for i in range(1, n+1):
        for j in range(1, m+1):

            if p[i - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

            else:
                dp[i][j] = p[i - 1] == (s[j - 1] or p[i - 1] == "?") and dp[i - 1][j - 1] 

    return dp[n][m]

    



def main():
    S1 = "ab*cd"
    S2 = "abdefcd"

    if wildcard_matching(S1, S2):
        print("String S1 and S2 do match")
    else:
        print("String S1 and S2 do not match")

if __name__ == "__main__":
    main()
            
        
        
