class UnionFind:
    '''
    Python implementation of Union-Find 
    algorithm to store a disjoint set.
    '''

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.count = size


    def find(self, X):
        if X == self.root[X]:
            return X

        self.root[X] = self.find(self.root[X])
        return self.root[X]

    def union(self, X, Y):
        rootX = self.find(X)
        rootY = self.find(Y)

        if rootX != rootY:
            if self.rank[X] > self.rank[Y]:
                self.root[rootY] = rootX

            elif self.rank[Y] > self.rank[X]:
                self.root[rootX] = rootY

            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

            self.count -= 1


    def getCount(self):
        return self.count


    
    