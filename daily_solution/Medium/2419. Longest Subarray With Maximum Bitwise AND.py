class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        longest = current = 0

        for num in nums:
            if num == max_val:
                current += 1
                longest = max(longest, current)
            else:
                current = 0

        return longest
