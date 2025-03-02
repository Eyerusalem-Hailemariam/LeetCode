class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points)):
            count = defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                    count[dist] += 1
            for count in count.values():
                result += count * (count - 1)
        return result