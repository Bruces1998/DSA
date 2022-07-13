def rotten_oranges(grid):
    if not grid:
        return 0
    
    n = len(grid)
    m = len(grid[0])

    rotten = []
    total = 0
    count = 0
    days = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                total+=1
            if grid[i][j] == 2:
                rotten.append((i, j))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while rotten != []:
        k = len(rotten)
        count += k
        while k:
            x, y = rotten.pop(0)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (nx < 0 || ny < 0 || nx >= m || ny >= n || grid[nx][ny] != 1):
                    continue
                grid[nx][ny] = 2
                rotten.append((nx, ny))
        if rotten != []:
            days += 1

    if count == total:
        return days

    return -1
