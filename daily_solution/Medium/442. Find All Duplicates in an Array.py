from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
       return [count for count,freq in Counter(nums).items() if freq>1]
