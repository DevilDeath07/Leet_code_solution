from itertools import groupby
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # Find maximum consecutive zeros
        conse_zero = max((len(list(group)) for key, group in groupby(nums) if key == 0), default=0)
        # Count total number of zeros
        count_zero = nums.count(0)
        # Create zero array (not needed for final count, but preserved for structure)
        zero_array = [0] * count_zero
        # Count zero-filled subarrays directly from the original array
        def count_zero_filled_subarrays(arr):
            count = 0
            streak = 0
            for num in arr:
                if num == 0:
                    streak += 1
                    count += streak
                else:
                    streak = 0
            return count
        return count_zero_filled_subarrays(nums)
