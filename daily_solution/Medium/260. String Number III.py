class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import Counter

        counter = Counter(nums)
        result =[]
        for count,freq in counter.items():
            if freq == 1:
                result.append(count)
        return result
