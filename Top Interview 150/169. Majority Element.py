from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_elem, max_freq = counter.most_common(1)[0]
        return max_elem
