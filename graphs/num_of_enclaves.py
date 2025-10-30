class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return -1

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            if grid[i][0] == 1:
                grid = self.dfs(i, 0, grid, n, m)
            
            if grid[i][m - 1] == 1:
                grid = self.dfs(i, m - 1, grid, n, m)

        
        for j in range(m):
            if grid[0][j] == 1:
                grid = self.dfs(0, j, grid, n, m)
            
            if grid[n - 1][j] == 1:
                grid = self.dfs(n - 1, j, grid, n, m)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1

        return count
        
    
    def dfs(self, i, j, board, n, m):
        if i >= n or i < 0 or j >= m  or j < 0 or board[i][j] != 1:
            return board

        board[i][j] = "."

        for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            row, col = i+dx, j+dy
            board = self.dfs(row, col, board, n, m )

        return board