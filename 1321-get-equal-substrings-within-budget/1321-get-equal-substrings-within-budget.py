class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        n = len(s)
        res = 0
        curCost = 0

        for right in range(n):
            curCost += abs(ord(s[right]) - ord(t[right]))

            while curCost > maxCost:
                curCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            res = max(res, right - left + 1)
        return res