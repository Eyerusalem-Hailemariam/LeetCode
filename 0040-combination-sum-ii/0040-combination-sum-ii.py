class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
    
        candidates.sort()
        
        dp = [set() for _ in range(target + 1)]
        dp[0].add(()) 
        
        for num in candidates:
            for j in range(target, num - 1, -1):
                for prev_comb in dp[j - num]:
                    dp[j].add(prev_comb + (num,))
                    
        return [list(comb) for comb in dp[target]]