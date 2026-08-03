class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        dp = [[] for _ in range(target + 1)]
        
        dp[0] = [[]]
        
        for candidate in candidates:
            for i in range(candidate, target + 1):
                for comb in dp[i - candidate]:
                    dp[i].append(comb + [candidate])
                    
        return dp[target]