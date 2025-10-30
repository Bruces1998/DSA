def allPaths(graphs):
    res = []

    def dfs(node, path):
        if node == len(graphs) - 1:
            res.append(path)
            return

        for neighbor in graphs[node]:
            dfs(neighbor, path + [neighbor])
    dfs(0, [0])
    return res        