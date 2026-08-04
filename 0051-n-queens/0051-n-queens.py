class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        cols = [False] * n
        pos_diag = [False] * (2 * n - 1)
        neg_diag = [False] * (2 * n - 1)
        
        queens = [-1] * n

        def backtrack(r):
            if r == n:
               
                board = []
                for c in queens:
                    row_str = "." * c + "Q" + "." * (n - 1 - c)
                    board.append(row_str)
                res.append(board)
                return

            for c in range(n):
                if cols[c] or pos_diag[r + c] or neg_diag[r - c + n - 1]:
                    continue

              
                cols[c] = True
                pos_diag[r + c] = True
                neg_diag[r - c + n - 1] = True
                queens[r] = c

                backtrack(r + 1)

                
                cols[c] = False
                pos_diag[r + c] = False
                neg_diag[r - c + n - 1] = False

        backtrack(0)
        return res