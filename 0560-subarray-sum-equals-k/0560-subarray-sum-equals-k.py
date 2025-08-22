class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefSum = {0: 1}
        n = len(nums)
        prefix = 0
        res = 0

        for i in range(n):
            prefix += nums[i]
            diff = prefix - k

            
            if diff in prefSum:
                res += prefSum[diff]
                
            prefSum[prefix] = 1 + prefSum.get(prefix, 0)
        return res