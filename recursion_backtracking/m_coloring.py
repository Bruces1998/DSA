def graph_col(graph, m, N):

    color = [0]*N
    if solve(0, color, m, N, graph):
        return True

    return False


def solve(node, color, m, N, graph):

    if node == N:
        return True

    for k in range(1, m):
        if isValid(node, k, graph, color, N):
            color[node] = k
            if solve(node+1, color, m, N, graph):
                return True

            color[node] = 0

    return False
    
def isValid(node, k, graph, color, N):
    for i in range(N):
        if i != node and graph[node][i] == 1 and color[i] == color[node]:
            return False

    return True
