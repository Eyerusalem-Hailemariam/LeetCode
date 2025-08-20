class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefSum = [0] * (n + 1)
        accmulator = 0

        for i in range(n):
            accmulator += nums[i]
            self.prefSum[i + 1] = accmulator
        print(self.prefSum)
        

    def sumRange(self, left: int, right: int) -> int:

            return self.prefSum[right + 1] - self.prefSum[left]
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)