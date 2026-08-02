class Solution:

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        
        def helper(s, right, left):
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            else:
                return s
            
            helper(s, right, left)
        helper(s, n - 1, 0) 