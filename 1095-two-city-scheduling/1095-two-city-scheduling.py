class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        
        n = len(costs) // 2
        total_costs = 0

        for i in range(n):
            total_costs += costs[i][0]
        for i in range(n, len(costs)):
            total_costs += costs[i][1]
        
        return total_costs


        