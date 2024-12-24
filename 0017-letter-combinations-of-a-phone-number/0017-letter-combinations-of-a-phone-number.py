class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = []
        
        def backtrack(index, current_combination):
            if index == len(digits):
                result.append("".join(current_combination))
                return
            
            letters = phone_map[digits[index]]
            
            for letter in letters:
                current_combination.append(letter) 
                backtrack(index + 1, current_combination) 
                current_combination.pop()  
      
        backtrack(0, [])
        return result
