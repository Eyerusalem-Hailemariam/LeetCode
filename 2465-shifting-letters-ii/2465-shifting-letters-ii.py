class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix_sum = [0] * (n + 1)

        for start, end, direction in shifts:
            prefix_sum[end + 1] += 1 if direction else -1
            prefix_sum[start] += -1 if direction else 1
        res = [ord(c) - ord('a') for c in s]
        diff = 0
        for i in reversed(range(len(prefix_sum))):
            diff += prefix_sum[i]

            res[i - 1] = (diff + res[i - 1]) % 26
        s = [chr(ord('a') + num) for num in res]
        return "".join(s)