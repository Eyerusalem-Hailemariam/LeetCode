class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        ans  = []

        for num in nums2:
            if not stack:
                stack.append(num)
            else:
                while stack and num > stack[-1]:
                    x = stack.pop()
                    d[x] = num
                stack.append(num)
                
        for num in nums1:
            if num not in d:
                ans.append(-1)
            else:
                ans.append(d[num])
        return ans





                