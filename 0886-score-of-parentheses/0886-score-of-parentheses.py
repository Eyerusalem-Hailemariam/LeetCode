class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0] 

        for char in s:
            if char == "(":
                stack.append(0)  
            else:
                last = stack.pop()  
                if last == 0:
                    score = 1 
                else:
                    score = 2 * last  
                stack[-1] += score  
        return stack[0]

        