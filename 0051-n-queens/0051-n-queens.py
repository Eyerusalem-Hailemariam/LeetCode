class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()       # columns that already have queens
        pos_diag = set()   # r + c diagonals
        neg_diag = set()   # r - c diagonals

        queens = [-1] * n  # queens[row] = column where queen is placed

        def backtrack(r):
            # All rows have queens placed
            if r == n:
                board = []

                for row in range(n):
                    line = ["."] * n
                    line[queens[row]] = "Q"
                    board.append("".join(line))

                res.append(board)
                return

            for c in range(n):
                # Check if this position is attacked
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Place queen
                queens[r] = c
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtrack(r + 1)

                # Remove queen (backtrack)
                queens[r] = -1
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)

        return res