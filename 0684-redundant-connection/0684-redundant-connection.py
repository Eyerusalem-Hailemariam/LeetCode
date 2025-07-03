class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = [i for i in range(n + 1)]
        rank = [1 for i in range(n + 1)]

        def find(n):
            if root[n] != n:
                root[n] = find(root[n])
            return root[n]

        def union(n1, n2):
            root_x, root_y = find(n1), find(n2)

            if root_x == root_y:
                return False
            else:
                if rank[root_x] > rank[root_y]:
                    root[root_y] = root_x
                    rank[root_x] += rank[root_y]
                else:
                    root[root_x] = root_y
                    rank[root_y] += rank[root_x]
            return True
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]