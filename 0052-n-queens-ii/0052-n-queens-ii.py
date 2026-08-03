class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        
        def backtrack(r, cols, diags1, diags2):
            nonlocal res
            if r == n:
                res += 1
                return
            
            available_positions = ((1 << n) - 1) & ~(cols | diags1 | diags2)
            
            while available_positions:
                position = available_positions & -available_positions
                
                available_positions -= position
               
                backtrack(
                    r + 1, 
                    cols | position, 
                    (diags1 | position) << 1, 
                    (diags2 | position) >> 1
                )
                
        backtrack(0, 0, 0, 0)
        return res