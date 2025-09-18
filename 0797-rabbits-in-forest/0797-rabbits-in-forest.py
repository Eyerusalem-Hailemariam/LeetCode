class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count_answers = Counter(answers)
        totals = 0

        for answer, freq in count_answers.items():
            group_size = answer + 1
            group = math.ceil(freq / group_size)
            totals += group * group_size
        return totals