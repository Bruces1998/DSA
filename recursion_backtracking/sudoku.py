def backtrack(row, col, board):
    while board[row][col] != '.':
        col += 1
        if col == 9:
            col, row = 0, row+1
        if row == 9:
            return True

    for ch in range(1, 10):
        if isValid(row, col, board, str(ch)):
            board[row][col] = str(ch)
            if backtrack(row, col, board):
                return True

    board[row][col] = '.'
    return False

def isValid(row, col, board, c):
    for i in range(9):
        if board[row][i] == c:
            return False
        
        if board[i][col] == c:
            return False
    row = row - (row%3)
    col = col - (col%3)
    for i in range(row, row+3):
        for j in range(col, col+3):
            if board[i][j] == c:
                return False

    return True

def solve(board):
    backtrack(0, 0, board)
    print(board)
            

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solve(board)