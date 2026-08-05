class Solution:
    def grayCode(self, n: int) -> list[int]:
        total_nums = 1 << n  # This is 2^n
        res = [0]
        visited = {0}
        
        def backtrack(curr: int) -> bool:
            if len(res) == total_nums:
               
                diff = curr ^ 0
                return (diff & (diff - 1)) == 0
            
            for i in range(n):
                next_num = curr ^ (1 << i) 
                
                if next_num not in visited:
                    visited.add(next_num)
                    res.append(next_num)
                    
                    if backtrack(next_num):
                        return True
                    
                
                    res.pop()
                    visited.remove(next_num)
                    
            return False
        
        backtrack(0)
        return res