class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i]))
        count = 0
        while len(heap) >= 2 and heap[0] < k:
            count +=1 
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            print(first, second)
            heapq.heappush(heap, (min(first, second) * 2 + max(first, second)))
        return count