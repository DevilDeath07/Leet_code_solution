from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p, q = None, None

        # Find first descent (p) and next ascent (q)
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] and p is None:
                p = i
            elif p is not None and nums[i] < nums[i+1]:
                q = i
                break

        if p is None or q is None:
            return False

        temp1 = nums[:p+1]
        temp2 = nums[p:q+1]
        temp3 = nums[q:]

        # Enforce minimum lengths
        if len(temp1) < 2 or len(temp2) < 2 or len(temp3) < 2:
            return False

        # Strict monotonicity checks
        def is_strictly_increasing(arr):
            return all(arr[i] < arr[i+1] for i in range(len(arr)-1))

        def is_strictly_decreasing(arr):
            return all(arr[i] > arr[i+1] for i in range(len(arr)-1))

        return (is_strictly_increasing(temp1) and
                is_strictly_decreasing(temp2) and
                is_strictly_increasing(temp3))
