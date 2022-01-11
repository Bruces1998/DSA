from typing import List

MAX = 5

def isSafe(row, col, m, n, visited):

    if(row == -1 or row == n or col == -1 or col == n
        or visited[row][col] or m[row][col] == 0):
        return False

    return True


