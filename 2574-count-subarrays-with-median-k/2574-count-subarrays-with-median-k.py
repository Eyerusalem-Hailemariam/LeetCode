class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        p = nums.index(k)
        dict_nary = defaultdict(int)
        z = 0
        count = 0
        for right in range(p, len(nums)):
            z += 1 if nums[right] > k else (-1 if nums[right] < k else 0)
            dict_nary[z] += 1
        z = 0
        for right in range(p, -1, -1):
            z += 1 if nums[right] > k else (-1 if nums[right] < k else 0)
            count += dict_nary[-z] + dict_nary[-z + 1]
        return count         