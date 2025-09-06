class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)

        for i in range(n - 2):
            c, b, a = nums[i], nums[i + 1], nums[i + 2]
            if c < a + b:
                return c + a + b
        return 0

        

