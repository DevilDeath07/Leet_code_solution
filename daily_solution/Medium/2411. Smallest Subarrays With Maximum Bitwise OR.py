class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_or = 0
        for num in nums:
            max_or |= num

        result = [1] * n
        last_occurrence = [-1] * 32  # Track latest index of each bit

        for i in range(n - 1, -1, -1):
            num = nums[i]
            for b in range(32):
                if num & (1 << b):
                    last_occurrence[b] = i

            farthest = i
            for b in range(32):
                if max_or & (1 << b):
                    if last_occurrence[b] != -1:
                        farthest = max(farthest, last_occurrence[b])

            result[i] = farthest - i + 1
        return result
