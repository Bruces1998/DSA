'''
Problem Link-https://leetcode.com/problems/koko-eating-bananas/
'''

def koko_eat(piles, H):
    def cannot_eat(K):
        hours = 0
        for x in piles:
            if x % K == 0:
                hours += x // K
            else:
                hours += x // K + 1
        return hours > H
    
    low, high = 1, max(piles)
    while low < high:
        mid = low + (high - low) // 2
        if cannot_eat(piles, H, mid):
            low = mid + 1
        else:
            high = mid
    return low