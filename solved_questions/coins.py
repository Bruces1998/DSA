def make_change(amount, denoms, index):
#     if memo[amount][index] > 0:
#         return memo[amount][index]
    if index >= len(denoms)-1:
        return 1
    deno = denoms[index]
    ways = 0
    i=0
    while(i * deno <= amount ):
        amtR = amount - (i * deno)
        ways+= make_change(amtR, denoms, index+1 )
        i+=1
#     memo[amount][index] = ways
    return ways

# import numpy as np
# memo = np.zeros((10001,4))
print(make_change(10000, [25, 10, 5, 1], 0))