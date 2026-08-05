class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        
        for i in range(1, n + 1):
            add_val = 1 << (i - 1)
        
            res += [x + add_val for x in reversed(res)]
            
        return res