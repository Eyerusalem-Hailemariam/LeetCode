class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        s_logs = "".join(logs)
        s_logs = s_logs.split("/")

        for log in s_logs:
            if log == "..":
                if stack:
                    stack.pop()
            elif log and log != ".":
                stack.append(log)
        return len(stack)
        