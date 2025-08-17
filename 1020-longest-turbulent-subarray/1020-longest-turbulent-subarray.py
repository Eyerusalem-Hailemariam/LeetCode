class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 1
        n = len(arr)
        prev = ""
        res = 1

        while right < n:
            if arr[right - 1] > arr[right] and prev != '>':
                res = max(res, right - left + 1)
                prev = ">"
                right += 1
            elif arr[right - 1] < arr[right] and prev != '<':
                res = max(res, right - left + 1) 
                prev = "<"
                right += 1
            else:
                right = right + 1 if arr[right - 1] == arr[right] else right
                left = right - 1
                prev = ""
        return res
        