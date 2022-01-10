from collections import defaultdict
import heapq
INT_MAX = 100000

'''
this algo gives the shortest between 
the source and the destination.
'''

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest, weight):

        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

    def dijkstra(self, src, dest):

        V = self.V
        dist = [INT_MAX]*(V)
        parent = [-1]*(V)

        dist[src] = 0

        minHeap =  [(0, src)]

        while minHeap != []:
            curr = heapq.heappop(minHeap)[1]

            for vertex in self.graph[curr]:
                if dist[vertex[0]] > dist[curr] + vertex[1]:
                    dist[vertex[0]] = dist[curr] + vertex[1]
                    parent[vertex[0]] = curr
                    heapq.heappush(minHeap, (dist[vertex[0]], vertex[0]))


         
        def print_parent(j):
            if parent[j] == -1:
                return 
            
            print_parent(parent[j])
            print(j,"->", end = " ")

        for i in range(self.V):
            print(src, "->", end=" ")
            print_parent(i)
            print("end")




graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.dijkstra(0, 8)
