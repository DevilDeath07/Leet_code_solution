from collections import Counter
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_count = len(Counter(nums))
        total = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if distinct_count == len(Counter(nums[i:j+1])):
                    total +=1
        return total

# in our code have time limit exceeding error

# solve the time limit exceeding error using this code

from collections import Counter
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_count = len(Counter(nums))
        total = 0
        n = len(nums)
        for i in range(n):
            freq = Counter()
            unique = 0
            for j in range(i, n):
                if freq[nums[j]] == 0:
                    unique += 1
                freq[nums[j]] += 1
                if unique == distinct_count:
                    total += 1
        return total
