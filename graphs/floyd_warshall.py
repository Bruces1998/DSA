'''
The algo is used to find the shortest 
distanece between all the vertices in a 
weighted graph. Cannot be used with 
negative edge graphs. 
'''

nv = 4
INF = 999

def floyd(G):

    dist = list(map(lambda i: list(map(lambda j:j, i)), G))
    print(dist)
    for k in range(nv):

        for i in range(nv):
            for j in range(nv):

                dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j])

    print_solution(dist)


def print_solution(distance):

    for i in range(nv):
        for j in range(nv):
            if distance[i][j] == INF:
                print("INF", end = " ")

            else:
                print(distance[i][j], end = " ")

        print(" ")

graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
floyd(graph)