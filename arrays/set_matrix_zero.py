'''
problem link-
https://leetcode.com/problems/set-matrix-zeroes/
'''

def setMatrixZeroes(arr):

    rowLength = len(arr)
    colLength = len(arr[0])

    rowVector = [0]*rowLength
    colVector = [0]*colLength

    #Setting up the row and column vectors
    for i in range(rowLength):
        for j in range(colLength):
            if arr[i][j] == 0:
                rowVector[i] = 1
                colVector[j] = 1

    #setting up all the rows based on rowVector
    for i in range(rowLength):
        if rowVector[i] == 1:
            for j in range(colLength):
                arr[i][j] = 0

    #setting up all the rows based on colVector
    for j in range(colLength):
        if colVector[j] == 1:
            for i in range(rowLength):
                arr[i][j] = 0


    return arr


arr = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(setMatrixZeroes(arr))