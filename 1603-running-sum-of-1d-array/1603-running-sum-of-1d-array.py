class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        sum_nums = 0

        for num in nums:
            sum_nums += num 
            res.append(sum_nums)

        return res