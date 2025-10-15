class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc[i] = inc[i + 1] + 1

        def is_valid(k):
            limit = n - 2 * k + 1
            for i in range(limit):
                if inc[i] >= k and inc[i + k] >= k:
                    return True
            return False

        low, high = 1, n // 2
        best_k = 0
        while low <= high:
            mid = (low + high) // 2
            if is_valid(mid):
                best_k = mid
                low = mid + 1
            else:
                high = mid - 1

        return best_k
