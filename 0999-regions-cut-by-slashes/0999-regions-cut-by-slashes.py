class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        roots = {}

        def find(x):
            if x not in roots:
                roots[x] = x
            while x != roots[x]:
                roots[x] = roots[roots[x]]  
                x = roots[x]
            return x

        def union(x, y):
            roots[find(x)] = find(y)

        length = len(grid)

        for i in range(length):
            for j in range(length):
                c = grid[i][j]
                if c == '/':
                    union((i, j, 'N'), (i, j, 'W'))
                    union((i, j, 'S'), (i, j, 'E'))
                elif c == '\\':
                    union((i, j, 'N'), (i, j, 'E'))
                    union((i, j, 'S'), (i, j, 'W'))
                elif c == ' ':
                    union((i, j, 'N'), (i, j, 'E'))
                    union((i, j, 'E'), (i, j, 'S'))
                    union((i, j, 'S'), (i, j, 'W'))
                    union((i, j, 'W'), (i, j, 'N'))

                if j > 0:
                    union((i, j - 1, 'E'), (i, j, 'W'))
                if i > 0:
                    union((i - 1, j, 'S'), (i, j, 'N'))

        return len(set(find(x) for x in roots))
