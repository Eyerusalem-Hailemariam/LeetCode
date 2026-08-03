class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        cols = set()
        pos_diag = set()
        neg_diag = set()
        
        # 1D array to track queen positions: queens[row] = col
        queens = [-1] * n

        def backtrack(r):
            if r == n:
                # We only build the board strings here at the very end
                board = []
                for c in queens:
                    row_str = "." * c + "Q" + "." * (n - 1 - c)
                    board.append(row_str)
                res.append(board)
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Place the queen in our 1D array
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                queens[r] = c

                backtrack(r + 1)

                # Backtrack
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                # No need to reset queens[r] because it just gets overwritten later

        backtrack(0)
        return res