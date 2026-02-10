#our solution original
from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        before = len(nums)
        # Deduplicate while preserving order
        seen = set()
        anums = []
        for x in nums:
            if x not in seen:
                seen.add(x)
                anums.append(x)
        after = len(anums)

        # Count duplicates
        dup_count = before - after
        if after == 1:
            return 0
        n = len(anums)
        result = []

        # Generate possible subarrays
        for start in range(n):
            for end in range(start + 1, n + 1):
                temp = anums[start:end]
                if len(temp) % 2 == 0:
                    even_odd = [1 if val % 2 == 0 else 0 for val in temp]
                    result.append(even_odd)

        def check_balanced_or_not(arr):
            count1 = arr.count(1)  # evens
            count0 = arr.count(0)  # odds
            if count1 == count0:
                return count1 + count0
            return 0  # return 0 instead of None

        count = 0
        for arr in result:
            count = max(count, check_balanced_or_not(arr))
        if count != 0: 
            return count + dup_count
        return 0

------------------------------------------(or)------------------------------------------------------------
#alteredversion 
from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            odd_count = {}
            even_count = {}
            for j in range(i, n):
                if nums[j] & 1:
                    odd_count[nums[j]] = odd_count.get(nums[j], 0) + 1
                else:
                    even_count[nums[j]] = even_count.get(nums[j], 0) + 1

                if len(odd_count) == len(even_count):
                    max_len = max(max_len, j - i + 1)

        return max_len

