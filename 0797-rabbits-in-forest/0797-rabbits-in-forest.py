class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        total = 0

        for x, count in freq.items():
            group_size = x + 1
            groups = (count + group_size - 1) // group_size  
            total += groups * group_size

        return total
