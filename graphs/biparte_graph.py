'''
If we are able to colour a graph with two 
colours such that no adjacent nodes have the 
same colour, it is called a bipartite graph.


Link to the problem based
on the following concept:
https://www.interviewbit.com/old/problems/two-teams/
'''
class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = [[0 for col in range(V)] for row in range(V)]
        self.colourArr = [-1 for i in range(self.V)]

    def isBipartiteUtilBFS(self, src):

        queue = []
        queue.append(src)

        while(queue):

            u = queue.pop()

            if self.graph[u][u] == 1:
                return False    
                #self loop
            
            for v in range(self.V):

                if (self.graph[u][v] == 1 and self.colourArr[v] == -1):
                    self.colourArr[v] = 1 - self.colourArr[u]
                    queue.append(v)

                elif (self.graph[u][v] == 1 and self.colourArr[v] == self.colourArr[u]):
                    return False



        return True

    def isBipartiteUtilDFS(self, u):
        for v in range(self.V):
            if (self.graph[u][v] == 1 and self.colourArr[v] == -1):
                    self.colourArr[v] = 1 - self.colourArr[u]
                    if not self.isBipartiteUtilDFS(v):
                        return False

            elif (self.graph[u][v] == 1 and self.colourArr[v] == self.colourArr[u]):
                return False

        return True

            
    


    def isBipartite(self):
        self.colourArr = [-1 for i in range(self.V)]
        for i in range(self.V):
            if self.colourArr[i] == -1:
                self.colourArr[i] = 1
                if not self.isBipartiteUtilBFS(i):
                    return False
        return True


g = Graph(4)
g.graph = [[0, 1, 0, 1],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [1, 0, 1, 0]]
 
if g.isBipartite():
    print("yes")
else:
    print("no")