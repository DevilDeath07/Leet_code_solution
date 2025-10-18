class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        count = 0
        previous_val = float('-inf')
        for num in nums:
            optimalValue = min(num + k, max(num - k, previous_val + 1));
            if optimalValue > previous_val:
                count +=1
                previous_val = optimalValue
        return count
