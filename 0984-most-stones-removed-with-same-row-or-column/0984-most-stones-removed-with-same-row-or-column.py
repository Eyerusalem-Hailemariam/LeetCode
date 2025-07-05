
class Solution:

    def __init__(self):
        self.root = []
        self.size = []
    
    def find(self, X):
        if X == self.root[X]:
            return X
        self.root[X] = self.find(self.root[X])  # Path compression
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

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        self.root = [i for i in range(n)]
        self.size = [1] * n
        
        X = {}
        Y = {}
        
        for i, (x, y) in enumerate(stones):
            if x in X:
                self.union(i, X[x])
            else:
                X[x] = i
            if y in Y:
                self.union(i, Y[y])
            else:
                Y[y] = i
       
        unique_roots = set()
        for i in range(n):
            unique_roots.add(self.find(i))
        
        return n - len(unique_roots)
