class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        candidates.sort()
        
        def backtrack(start: int, current_combination: list[int], current_sum: int):
            if current_sum == target:
                results.append(list(current_combination))
                return

            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
        
                if current_sum + candidates[i] > target:
                    break
      
                current_combination.append(candidates[i])
                
             
                backtrack(i + 1, current_combination, current_sum + candidates[i])
                
           
                current_combination.pop()
        
        backtrack(0, [], 0)
        return results