class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        res = []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        def backtrack(index, curr):
            if len(digits) == len(curr):
                res.append("".join(curr))
                return

            for letter in phone_map[digits[index]]:
                curr.append(letter)
                backtrack(index + 1, curr)
                curr.pop()
            
        backtrack(0, [])
        return res
