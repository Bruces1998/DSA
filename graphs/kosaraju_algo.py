from collections import defaultdict
'''
The idea behind the algo is that
first you have to find the topological 
sort of the graph, then transpose the 
graph and finally carry out dfs of the 
topo order elements one by one
'''
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    #algo to carry out dfs of the graph
    def dfsUtil(self, v, visited):

        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfsUtil(i, visited)

    #Algo to caryy out the topological order sorting
    def fillOrder(self, v, visited, stack):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)


        stack.append(v)

    #function to get the transpose
    def getTranspose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)

        return g

    #binding function
    def printSCCs(self):

        stack = []
        visited = [False]*self.V

        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)


        gr = self.getTranspose()
        visited = [False]*self.V 

        while stack:
            i = stack.pop(-1)
            if visited[i] == False:
                gr.dfsUtil(i, visited)
                print("")

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
 
print ("Following are strongly connected components " +
                           "in given graph")
g.printSCCs()

