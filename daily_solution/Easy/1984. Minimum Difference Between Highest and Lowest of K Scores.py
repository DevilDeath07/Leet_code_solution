class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = float('inf')
        for i in range(len(nums)-k+1):
            temp = nums[i+k-1]-nums[i]
            result = min(temp, result)
        return result
