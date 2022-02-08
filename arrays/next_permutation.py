'''
Problem Link:
https://leetcode.com/problems/next-permutation/submissions/
'''

def nextPermut(num):
    i = len(num) - 1
    while(i > -1 and num[i] == max(num[i:])):
        i -= 1
    
    if i == -1:
        return sorted(num)
    
    curr = len(num) - 1

    while(num[curr]<=num[i]):
        curr -= 1

    num[i], num[curr] = num[curr], num[i]
    num[i+1:] = sorted(num[i+1:])
    return num

