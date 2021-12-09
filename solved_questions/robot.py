import numpy as np
import time

def get_path( arr, row, col, path):
    isori = None

    if col < 0 or row < 0:
        return False

    # if arr[row][col]==-1:
    #     return False

    if row==0 and col==0:
        isori = True

    if (isori or get_path(arr, row, col-1, path) or get_path(arr, row-1, col, path)):
        path.append((row, col))
        return True

    # arr[row][col]=-1
    return False

def robot(row, col):
    if row==0 or col==0:
        return False
    arr = np.zeros((row, col))
    path = []
    if (get_path(arr, row-1, col-1,path)):
        return path
    return null

if __name__ == "__main__":
    a = time.time()
    ans = robot(400,50)
    print(ans)
    b = time.time()
    print("{:.5f}".format(b-a))
