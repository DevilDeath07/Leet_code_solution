from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n =  int(len(nums)/2)
        counter = Counter(nums)
        for ele,freq in counter.items():
            if freq == n:
                return ele
