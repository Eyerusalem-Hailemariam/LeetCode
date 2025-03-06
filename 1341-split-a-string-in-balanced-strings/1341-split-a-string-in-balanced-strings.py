class Solution:
    def balancedStringSplit(self, s: str) -> int:
        str_R = 0
        str_L = 0
        count = 0
        for string in s:
            if string == "R":
                str_R += 1
            else:
                str_L += 1

            if str_R == str_L:
                count += 1
        return count


        