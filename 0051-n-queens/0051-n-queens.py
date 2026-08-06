class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res =[]
        col = [False] * n
        pos_diag = [False] * (2 * n - 1)
        neg_diag = [False] * (2 * n - 1)

        queen = [-1] * n

        def backtrack(r):
            if r == n:
                board = []
                for c in queen:
                    row_string = "." * c + "Q" + "." * (n - 1 - c)
                    board.append(row_string)
                res.append(board)

            
            for c in range(n):
                if col[c] or pos_diag[r + c] or neg_diag[r - c + n -1]:
                    continue
                
                col[c] = True
                pos_diag[r + c] = True
                neg_diag[r - c + n - 1] = True
                queen[r] = c

                backtrack(r + 1)

                col[c] = False
                pos_diag[r + c] = False
                neg_diag[r - c + n -1 ] = False

        backtrack(0)
        return res