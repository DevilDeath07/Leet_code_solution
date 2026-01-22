from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check(arr: List[int]) -> bool:
            """Check if the array is non-decreasing."""
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        ans = 0
        n = len(nums)

        while not check(nums):
            # Find the pair with minimum sum
            min_index = 0
            for i in range(1, n - 1):
                if nums[i] + nums[i + 1] < nums[min_index] + nums[min_index + 1]:
                    min_index = i

            # Merge the pair
            nums[min_index] += nums[min_index + 1]

            # Shift left from min_index+1
            for i in range(min_index + 1, n - 1):
                nums[i] = nums[i + 1]

            # Reduce logical length by 1
            n -= 1
            nums.pop()  # remove last element physically

            ans += 1

        return ans
