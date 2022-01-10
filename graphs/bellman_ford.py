'''
Just like Djikstra's algo, Bellman
ford's algo is also used to find out 
the shortest distance from source to 
all the other nodes in the graph, but
it's time complexity is O(VE) as 
compared to O(V+E) of Djikstra's.
'''
from collections import defaultdict
INT_MAX = 1000000

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # def addEdge(self, u, v, w):
    #     self.graph(append([u, v, w])

    def printArr(self, dist):
        print("Vertex Distnce from Source to Distance")
        for i in range(self.V):
            print("{}\t{}\t".format(i, dist[i]))

    def bellman(self, src):
        dist = [INT_MAX]*self.V
        dist[src] = 0

        for _ in range(self.V - 1):

            for u, v, w in self.graph:
                if dist[u] != INT_MAX and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w


        for u, v, w in self.graph:
            if dist[u] != INT_MAX and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        
        self.printArr(dist)


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
 
# Print the solution
g.bellman(0)



    