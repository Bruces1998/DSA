'''
The algorithm here finds out the mst
using the kruskal's algo. The idea behind
is using union find and sorting.
'''
from union_find_implementation import UnionFind

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])


    def kruskal(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key = lambda item: item[2])

        union = UnionFind(self.V)

        while e < self.V -1:
            u, v, w = self.graph[i]
            i += 1
            x = union.find(u)
            y = union.find(v)

            if x != y:
                e += 1
                result.append([u, v, w])
                union.union(x, y)

        minimumCost = 0
        print ("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)



g = Graph(12)
g.addEdge(0, 1, 10)
g.addEdge(0, 6, 10)
g.addEdge(0, 7, 10)
g.addEdge(1, 2, 10)
g.addEdge(1, 5, 10)
g.addEdge(2, 3, 10)
g.addEdge(2, 4, 10)
g.addEdge(7, 8, 10)
g.addEdge(7, 11, 10)
g.addEdge(8, 9, 10)
g.addEdge(8, 10, 10)
g.addEdge(8, 11, 10)
 
# Function call
g.kruskal()