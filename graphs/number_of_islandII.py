
class UnionFind:
    '''
    Python implementation of Union-Find 
    algorithm to store a disjoint set.
    '''

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1 for i in range(size)]
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
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]

            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]

            self.count -= 1


    def getCount(self):
        return self.count
class Solution:
    def removeStones( stones: list[list[int]]) -> int:

        n = len(stones)
        UF = UnionFind(n)
        _count = 1
        if n >= 1:
            print(1)
        for i in range(1, n):
            for j in range(i):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    rootX = UF.find(i)
                    rootY = UF.find(j)

                    if rootX != rootY:
                        UF.union(i, j)


            _count += 1
            print(UF.getCount() - (n - _count))

                

        


Solution.removeStones([[0, 0], [0, 0], [1, 1],[1,0], [0, 1], [0, 3], [1, 3], [0, 4], [3, 2], [2, 2], [1, 2], [0, 2]])
