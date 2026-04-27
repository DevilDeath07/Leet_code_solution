class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        total = sum(nums)

        # If already divisible
        if total % k == 0:
            return count

        # Keep reducing until divisible
        while total % k != 0:
            total -= 1   # one operation reduces sum by 1
            count += 1

        return count
