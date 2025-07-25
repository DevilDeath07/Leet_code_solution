class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            return [list(subset) for subset in chain.from_iterable(combinations(nums, r) 
            for r in range(len(nums)+1))]
