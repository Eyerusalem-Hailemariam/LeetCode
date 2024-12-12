class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
         nums.sort()
         left = 0
         right = len(nums) - 1
         count = 0
    
    # Step 3: Use two pointers to find and count pairs
         while left < right:
            if nums[left] + nums[right] < target:
            # All pairs from left to right-1 will be valid
                   count += (right - left)
                   left += 1
            else:
                   right -= 1
    
         return count