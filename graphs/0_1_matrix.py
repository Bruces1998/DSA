class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        ans = []

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    mat[i][j] = findNearest(i, j, mat, n, m)
    
        return mat

        
def findNearest(row, col, mat, n, m):

    queue = [(row, col, 0)]
    visited = {}

    while queue:
        
        i, j, dist = queue.pop(0)
        visited[(i, j)] = 1

        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            if i+dx < 0 or i+dx>=n or j+dy < 0 or j+dy>=m:
                continue

            if mat[i+dx][j+dy] == 0:
                return dist + 1

            if visited.get((i+dx, j+dy)) is None :
                queue.append((i+dx, j+dy, dist + 1))

    return -1
        