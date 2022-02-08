def rotate(arr):
    row = len(arr)
    col = len(arr[0])

    for i in range(row):
        for j in range(i, col):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    
    for i in range(row):
        for j in range(col//2):
            arr[i][j], arr[i][col-1-j] = arr[i][col-1-j], arr[i][j]

    
    return arr