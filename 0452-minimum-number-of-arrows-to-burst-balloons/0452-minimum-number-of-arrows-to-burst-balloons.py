class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])

        inital = 1
        position = points[0][1]

        for xstart, xend in points:
            if xstart <= position <= xend:
                continue
            else:
                inital += 1
                position = xend
        return inital
      