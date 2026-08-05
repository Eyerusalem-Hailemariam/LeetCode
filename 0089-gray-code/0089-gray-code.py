class Solution:
    def grayCode(self, n: int) -> list[int]:
   
        if n == 0:
            return [0]
        
        prev_sequence = self.grayCode(n - 1)
        
      
        add_val = 1 << (n - 1)
        
        mirrored_part = [x + add_val for x in reversed(prev_sequence)]
        
        return prev_sequence + mirrored_part