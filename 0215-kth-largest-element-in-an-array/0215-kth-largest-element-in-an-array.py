class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def heapfiy(nums, n, i):
            largest = i
            left = 2 * largest + 1
            right = 2 * largest + 2

            if left < n and nums[left] > nums[largest]:
                largest =  left
            if right < n and nums[right] > nums[largest]:
                largest = right
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapfiy(nums, n, largest)
        
        for i in range(n // 2 - 1, -1, -1):
            heapfiy(nums, n, i)
        
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]

            heapfiy(nums, i, 0)
        print(nums)

        return nums[-k]