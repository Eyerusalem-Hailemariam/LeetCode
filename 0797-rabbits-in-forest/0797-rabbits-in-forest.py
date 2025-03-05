class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count_answers = Counter(answers)
        total_rabits = 0
        for ans, count in count_answers.items():
            group_size = ans + 1
            num_groups = ceil(count / group_size)
            total_rabits += num_groups * group_size

        return total_rabits

