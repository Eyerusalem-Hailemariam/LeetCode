class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3" : "def", "4":"ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9" : "wxyz"
        }

        dp = [""]

        for digit in digits:
            next_combination = []
            for combination in dp:
                for letter in phone_map[digit]:
                    next_combination.append(combination + letter)
        
            dp = next_combination
        return  dp