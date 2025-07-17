class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter

        counter = Counter(nums)
        for count,freq in counter.items():
            if freq == 1:
                return count
