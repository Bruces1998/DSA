def isSafe(x, y, board):
    n = len(board)
    m = len(board[0])

    row = x
    col = y

    while row>=0 and col >= 0:
        if board[row][col] == "Q":
            return False
        
        row -= 1
        col -= 1

    row = x
    col = y

    while row>=0 and col >= 0:
        if board[row][col] == "Q":
            return False
        
        col -= 1

    row = x
    col = y

    while row<n and col >= 0:
        if board[row][col] == "Q":
            return False
        
        row += 1
        col -= 1

    return True

    

def solve(board, n, col, ans):
    print(board)
    
    if col == n:
        ans.append(board)
        return
    
    for row in range(len(board)):
        if isSafe(row, col, board):
            board[row][col] = "Q"
            solve(board, n, col+1, ans)
            board[row][col] = "."



def solveNQueens(n):
    ans = []
    board = [["." for _ in range(n)] for _ in range(n)]
    solve(board, n, 0, ans)
    return ans

n = 4
ans = solveNQueens(n)
print(ans)
for i in range(len(ans)):
    print(f"Arrangement {i+1}")
    for j in range(len(ans[0])):
        print(ans[i][j])
    print()