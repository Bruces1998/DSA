def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(4):
        for i in range(4):
            for j in range(4):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                
    return distance     
graph = [[0, 5, 7, 1], [9, 0, 15, 13], [4, 14, 0, 2], [3, 8, 1, 0]]
print(floyd_warshall(graph))
