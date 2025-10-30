import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        n = len(heights)
        m = len(heights[0])
        
        dist = {

        }

        for i in range(n):
            for j in range(m):
                dist[(i, j)] = float("inf")

        dist[(0, 0)] = 0

        minHeap = []
        heapq.heappush(minHeap, (0, (0, 0)))

        while minHeap != []:
            row, col = heapq.heappop(minHeap)[1]

            for x, y in valid_neigh(row, col, n, m):
                if dist[(x, y)] > max(dist[(row, col)], abs(heights[x][y] - heights[row][col])):
                    dist[(x, y)] = max(dist[(row, col)], abs(heights[x][y] - heights[row][col]))
                    heapq.heappush(minHeap, (dist[(x, y)], (x, y)))

        return dist[(n -1, m - 1)]


def valid_neigh(row, col, n, m):
            
    valid_list = []
    for dx, dy in [ (-1, 0), (0, -1), (0, 1), (1, 0)]:
        if row+dx < 0 or row+dx >= n or col+dy < 0 or col+dy >=m:
            continue
        valid_list.append((row+dx, col+dy))

    return valid_list