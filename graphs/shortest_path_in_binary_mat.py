class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1 

        ans = float("inf")
        
        def valid_neigh(row, col):
            
            valid_list = []
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if row+dx < 0 or row+dx >= n or col+dy < 0 or col+dy >=n:
                    continue
                valid_list.append((row+dx, col+dy))

            return valid_list
        
        queue = [(1, 0, 0)]
        visited = set((0, 0))

        while queue:
            level, row, col = queue.pop(0)
            if row == n - 1 and col == n - 1:
                ans = min(ans, level)

            
            for i, j in valid_neigh(row, col):
                
                #if (i, j) not in visited:
                if grid[i][j] != 1:
                    queue.append((level + 1, i, j))
                    #visited.add((i, j))
                    grid[i][j] = 1

                    
        if ans == float("inf"):
            return -1
        return ans