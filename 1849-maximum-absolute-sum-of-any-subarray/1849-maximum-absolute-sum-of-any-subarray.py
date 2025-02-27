class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        max_sum, min_sum = 0, 0
        max_f, min_f = 0, 0
        
        for num in nums:
            max_f = max(0, max_f + num)  
            min_f = min(0, min_f + num)  
            
            max_sum = max(max_sum, max_f)
            min_sum = min(min_sum, min_f)
        
        return max(max_sum, abs(min_sum))
