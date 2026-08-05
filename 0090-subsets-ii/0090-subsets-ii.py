class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        subsets = [[]]
        start_idx = 0
        end_idx = 0
        
        for i in range(len(nums)):
       
            if i > 0 and nums[i] == nums[i - 1]:
                start_idx = end_idx
            else:
                start_idx = 0
                
            end_idx = len(subsets)
            
            for j in range(start_idx, end_idx):
                new_subset = subsets[j] + [nums[i]]
                subsets.append(new_subset)
                
        return subsets