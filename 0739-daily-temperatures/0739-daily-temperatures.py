class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temperature = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)

            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    x = stack.pop()
                    temperature[x] = i - x
                stack.append(i)
        return temperature 
                    


