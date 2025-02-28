class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        result = []
        total = 0

        for i in range(len(s) - 1, -1, -1):
            total += shifts[i]
            new_char = chr(((ord(s[i]) - ord('a') + total) % 26) + ord('a'))

            result.append(new_char)
        return "".join(result)[::-1]