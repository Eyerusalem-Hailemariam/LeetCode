class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []

        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        
        count = 0
        while heap:
            val, row, col = heapq.heappop(heap)
            count += 1

            if count == k:
                return val

            if col + 1 < n:
                heapq.heappush(heap, ((matrix[row][col + 1], row, col + 1)))



        