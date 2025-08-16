class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        n = len(fruits)
        res = 0

        left = 0
        for right in range(n):
            window[fruits[right]] += 1
            
            while len(window) > 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                left += 1
                    
            res = max(right - left + 1, res)
            
        return res    

            