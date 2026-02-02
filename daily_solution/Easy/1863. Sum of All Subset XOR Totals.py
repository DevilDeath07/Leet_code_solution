import functools
import operator
from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []

        # generate subsets of all possible lengths
        for r in range(1, len(nums)+1):   # start from 1 to avoid empty subset
            for combo in combinations(nums, r):
                subsets.append(list(combo))


        result = 0
        for arr in subsets:
            result += functools.reduce(operator.xor, arr, 0)
        return result
