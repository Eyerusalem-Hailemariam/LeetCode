class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_ones = sum(nums)
        left = 0
        right = total_ones
        max_score = -1
        score = 0

        result = []
        for i in range(n + 1):
            score = left + right
            if score > max_score:
                max_score = score
                result = [i]
            elif score == max_score:
                result.append(i)

            if i < len(nums):
                if nums[i] == 0:
                    left += 1
                elif nums[i] == 1:
                    right -= 1
        return result 

        