class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:

        n = len(grid)
        candidates = []
        for i in range(n):
            row = sorted(grid[i], reverse=True)
            for j in range(min(len(row), limits[i])):
                candidates.append(row[j])
        candidates.sort(reverse=True)
        
      
        return sum(candidates[:k])
