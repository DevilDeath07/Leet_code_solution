class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 1000000007
        left=0
        right=len(nums) - 1
        result = 0
        powers = [1] * len(nums)

        # Precompute powers of 2
        for i in range(1, len(nums)):
            powers[i] = (powers[i-1] * 2)

        while left <= right:
            if nums[left] + nums[right] <= target:
                result += powers[right - left]
                result %= mod
                left += 1
            else:
                right -= 1

        return result
