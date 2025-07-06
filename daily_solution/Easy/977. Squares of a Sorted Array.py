import numpy as np
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = sorted(np.square(nums))
        return [int(x) for x in result]
        
