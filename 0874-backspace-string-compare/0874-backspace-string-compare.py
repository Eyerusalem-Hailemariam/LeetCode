class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stack(a):
            stack = []
            for string in a:
                if not stack and string != "#":
                    stack.append(string)
                else:
                    if string == "#":
                        if stack:
                            stack.pop()
                    elif string != "#":
                        stack.append(string)
            return stack
        return stack(s) == stack(t)
        


                    



        