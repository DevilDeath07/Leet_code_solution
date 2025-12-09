import itertools
from collections import Counter
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        count = 0
        
        # Start with all values in the "right side"
        right_count = Counter(nums)
        left_count = Counter()
        
        for j in range(n):
            x = nums[j]
            right_count[x] -= 1   # remove current element from right side
            
            need = 2 * x
            left = left_count[need]      # how many 2*x before j
            right = right_count[need]    # how many 2*x after j
            
            count = (count + left * right) % MOD
            
            left_count[x] += 1   # add current element to left side
        
        return count
