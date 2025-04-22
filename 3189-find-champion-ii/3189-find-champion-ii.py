class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        has_lost = set()

        for winner, loser in edges:
            has_lost.add(loser)

        potential_champions = [i for i in range(n) if i not in has_lost]

        if len(potential_champions) == 1:
            return potential_champions[0]
        else:
            return -1
