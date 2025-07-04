class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(4 * n * n)

        for i in range(n):
            for j in range(n):
                index = 4 * (i * n + j)
                c = grid[i][j]

                if c == ' ':
                    uf.union(index + 0, index + 1)
                    uf.union(index + 1, index + 2)
                    uf.union(index + 2, index + 3)
                elif c == '/':
                    uf.union(index + 0, index + 3)
                    uf.union(index + 1, index + 2)
                elif c == '\\':
                    uf.union(index + 0, index + 1)
                    uf.union(index + 2, index + 3)

              
                if i + 1 < n:
                    uf.union(index + 2, (index + 4 * n) + 0)
               
                if j + 1 < n:
                    uf.union(index + 1, (index + 4) + 3)

        return uf.count()

class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    def count(self):
        return sum(1 for i in range(len(self.parent)) if self.find(i) == i)
    