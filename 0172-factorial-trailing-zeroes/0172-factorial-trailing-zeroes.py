class Solution:
    def trailingZeroes(self, n: int) -> int:
        def countfive(n):
            if n == 0:
                return 0

            return (n // 5) + countfive(n // 5)
        
        return countfive(n)
        
    
