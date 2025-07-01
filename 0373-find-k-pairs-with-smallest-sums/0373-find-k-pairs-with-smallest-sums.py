class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        n1, n2 = len(nums1), len(nums2)
        if not nums1 or not nums2:
            return res

        heap = []
        visited = set()

        heapq.heappush(heap, (nums1[0]+nums2[0], 0, 0))
        visited.add((0,0))

        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if j + 1 < n2 and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i, j+1))

            if i + 1 < n1 and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
                visited.add((i+1, j))

        return res




        