def isValid(i, j, r, c):
    if i < 0 or i >= r or j < 0 or j >= c:
        return False

    return True


def dfs(word, m, i, j, arr):
    if not isValid(i, j, len(arr), len(arr[0])):
        return False
    if m == len(word):
        return True
    if word[m] != arr[i][j]:
        return False

    v1 = dfs(word, m+1, i+1, j, arr)
    v2 = dfs(word, m+1, i-1, j, arr)
    v3 = dfs(word, m+1, i, j+1, arr)
    v4 = dfs(word, m+1, i, j-1, arr)

    if v1 or v2 or v3 or v4:
        return True

    return False


def solve():
    A = [
    "ABCE",
    "SFCS",
    "ADEE"
    ]
    B = input('Word: ')

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == B[0]:
                if dfs(B, 0, i, j, A):
                    return True

    return False

print(solve())
                
