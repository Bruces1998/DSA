'''
Problem Link-
https://leetcode.com/problems/pascals-triangle/
'''
def solve(A):
    if A == 0:
        return []

    ans = [[1]]

    for i in range(1, A):
        curr = ans[-1]
        temp_ans = [1]

        for j in range(1, len(curr)):
            temp_ans.append(curr[j]+curr[j-1])
        
        temp_ans.append(1)
        ans.append(temp_ans)

    return ans