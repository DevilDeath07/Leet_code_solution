class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return nums
        indexed_nums = list(enumerate(nums))
        top_k = sorted(indexed_nums, key=lambda x: x[1], reverse= True)[:k]
        top_k_sorted = sorted(top_k, key=lambda x: x[0])
        return [i for j,i in top_k_sorted]
