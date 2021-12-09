def solve(board, col):
    if col>=len(board):
        return True

    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1

            if solve(board, col+1):
                return True

            board[i][col] = 0

    return False


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i]==1:
            return False

    for i, j in zip(range(row,-1,-1), range(col,-1, -1)):
        if board[i][j]==1:
            return False

    for i, j in zip(range(row,len(board),-1), range(col,-1, -1)):
        if board[i][j]==1:
            return False

    return True


def solveNQ():
    board = [ [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    b1 = board
    for i in range(len(b1)):
        if solve(b1, i) == False:
            print ("Solution does not exist")
            b1 = board
        else:


            print(board)
            b1 = board

# Driver Code
solveNQ()
