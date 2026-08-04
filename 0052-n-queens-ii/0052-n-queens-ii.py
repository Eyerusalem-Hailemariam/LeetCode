class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        
        cols = [False] * n
        pos_diag = [False] * (2 * n - 1)
        neg_diag = [False] * (2 * n - 1)

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return

            for c in range(n):
                if cols[c] or pos_diag[r + c] or neg_diag[r - c + n - 1]:
                    continue

                cols[c] = True
                pos_diag[r + c] = True
                neg_diag[r - c + n - 1] = True

                backtrack(r + 1)

                cols[c] = False
                pos_diag[r + c] = False
                neg_diag[r - c + n - 1] = False

        backtrack(0)
        return res