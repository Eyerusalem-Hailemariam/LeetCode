class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0

        while left <= right:
            area = (right - left) * min(height[left], height[right])
            res = max(area, res)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res      