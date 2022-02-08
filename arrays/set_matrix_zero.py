'''
problem link-
https://leetcode.com/problems/set-matrix-zeroes/
'''

def zetZeroes(arr):
    row = len(arr)
    col = len(arr[0])

    row_vec = [0]*row
    col_vec = [0]*col

    for i in range(row):
        for j in range(col):
            if arr[i][j] == 0:
                row_vec[i] = 1
                col_vec[j] = 1

    for i in range(row):
        if row_vec[i] == 1:
            for j in range(cols):
                arr[i][j] = 0

    
        if col_vec[j] == 1:
            for i in range(row):
                arr[i][j] = 0


    return arr