class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def house_rob(arrs):
            prev2 = 0
            prev1 = 0

            for money in arrs:
                curr = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = curr
            return prev1
        return max( house_rob(nums[:-1]), house_rob(nums[1:]))
