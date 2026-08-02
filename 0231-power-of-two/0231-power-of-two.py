class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == 1:
        #     return True
        # if n == 0:
        #     return False

        # return  self.isPowerOfTwo(n // 2) if n % 2 == 0 else False 

        return True if n > 0  and (n & (n - 1)) == 0  else False

