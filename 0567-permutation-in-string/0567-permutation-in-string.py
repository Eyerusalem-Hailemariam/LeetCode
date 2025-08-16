class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        count_s2 = defaultdict(int)
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        for i in range(n):
            count_s2[s2[i]] += 1
        if count_s1 == count_s2:
            return True
        
        left = 0
        for right in range(n, m):
            count_s2[s2[right]] += 1
            count_s2[s2[left]] -= 1
            if count_s2[s2[left]] == 0:
                del count_s2[s2[left]]
            left += 1
            
            if count_s1 == count_s2:
                return True
        return False
