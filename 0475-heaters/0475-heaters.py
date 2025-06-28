class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        
        for house in houses:
          
            pos = bisect.bisect_left(heaters, house)
            
           
            left_dist = float('inf') if pos == 0 else house - heaters[pos - 1]
            right_dist = float('inf') if pos == len(heaters) else heaters[pos] - house
            
          
            min_dist = min(left_dist, right_dist)
            
            
            radius = max(radius, min_dist)
        
        return radius
