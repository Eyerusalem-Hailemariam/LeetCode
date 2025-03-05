from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[0])
        count = 1
        p = points[0]
        
        for i in range(1, len(points)):
            if points[i][0] <= p[1]:
                p[1] = min(p[1], points[i][1])
            else:
                count += 1
                p = points[i]
        
        return count





