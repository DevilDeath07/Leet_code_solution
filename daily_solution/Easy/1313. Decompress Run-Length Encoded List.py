import numpy as np
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        n= len(nums)
        if (n%2!=0) and (n<2):
            return result
        for i in range(n//2):
            [freq, val] = nums[2*i], nums[2*i+1]
            temp = np.full(freq, val)
            result.append(temp)
        flat_array = np.concatenate(result)
        return flat_array.tolist()

        
