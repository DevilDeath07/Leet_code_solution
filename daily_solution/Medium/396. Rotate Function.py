class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        # F(0)
        f0 = sum(i * num for i, num in enumerate(nums))
        result = f0
        current = f0
        
        # Use recurrence instead of recomputing
        for k in range(1, n):
            current = current + total_sum - n * nums[-k]
            result = max(result, current)
        
        return result

-----------------------------------------------------(or)--------------------------------------------------

from collections import deque

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        dq = deque(nums)
        n = len(nums)
        
        result = float('-inf')
        
        # Try exactly n rotations
        for _ in range(n):
            temp2 = 0
            # compute weighted sum for current rotation
            for i in range(n):
                temp2 += i * dq[i]
            result = max(result, temp2)
            dq.rotate(1)  # move to next rotation
        
        return result
