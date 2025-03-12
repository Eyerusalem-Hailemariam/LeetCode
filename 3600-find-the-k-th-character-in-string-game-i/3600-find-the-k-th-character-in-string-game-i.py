class Solution:
    def kthCharacter(self, k: int) -> str:
        def solv(s, k):
            while len(s) <= k:
                res = []
                l = len(s) -1 
                while  l >= 0:
                    new_char = chr(((ord(s[l]) - 97 + 1) % 26) + 97)
                    res.append(new_char)
                    l -= 1
                s += res[::-1]
            return s[k - 1]
        x = solv(['a'], k)
        return x
        