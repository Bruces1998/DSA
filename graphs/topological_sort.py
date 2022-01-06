
from collections import defaultdict 
import time

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def topologicalSortUtil(self, v, visited, stack):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)


        stack.append(v)

    def topologicalSort(self):

        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        print(stack[::-1])


    def topoSortKahn(self):
        in_degree = [0] * self.V

        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)
        top_order = []
        while queue:
            curr = queue.pop(0)
            top_order.append(curr)

            for vertex in self.graph[curr]:
                in_degree[vertex] -= 1
                if in_degree[vertex] == 0:
                    queue.append(vertex)

        if len(top_order) != self.V:
            return []

        return top_order


# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
 
print ("Following is a Topological Sort of the given graph")
 
# Function Call()
start = time.time()
g.topologicalSort()
print((time.time() - start)*1000)

print ("Following is a Topological Sort of the given graph using Kahn's")
start = time.time()
print(g.topoSortKahn())
print((time.time() - start)*1000)

                
