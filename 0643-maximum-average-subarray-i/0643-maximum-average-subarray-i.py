class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        max_sum = 0

        for i in range(k):
            window_sum += nums[i]
        

        max_sum = window_sum
        left = 0
        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[left]

            max_sum = max(max_sum, window_sum)
            left += 1
        return max_sum / k 
        