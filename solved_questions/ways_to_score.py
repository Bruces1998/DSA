memo = {}
def score(n):
    if n ==0:
        return 1
    if n <0:
        return 0
    if n not in memo:
        memo[n] = score(n - 3) + score( n -5) +  score(n - 10)
    return memo[n]


print(score(15))
