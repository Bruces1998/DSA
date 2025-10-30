'''
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
The idea behind the question is that the minimun capacity for the ship 
can be the largest weighted box taking each box individually and maximum
capacity for the ship can be the summation of all the weights taking every
box at the same time. Using these two lower and upper bounds, we apply binary 
search on the capcity and try to find the minimum weight that satifies the
day requirement.

Question https://leetcode.com/problems/split-array-largest-sum/ is a similar
problem where we can imagine each subarray as the boxes being taken on one 
particular day. 
'''

def shipWithinDays(weights: List[int], D: int) -> int:
    def feasible(capacity) -> bool:
        days = 1
        total = 0
        for weight in weights:
            total += weight
            if total > capacity:  # too heavy, wait for the next day
                total = weight
                days += 1
                if days > D:  # cannot ship within D days
                    return False
        return True

    left, right = max(weights), sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left

