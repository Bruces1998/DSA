def countPaths(i, j, n, m):
    if i == n-1 and j == m-1:
        return 1

    if i >=n or j>=m:
        return 0

    return countPaths(i+1, j, n, m)+countPaths(i, j+1, n, m)


def 