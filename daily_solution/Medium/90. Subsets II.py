from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort to group duplicates
        result = []

        def backtrack(start, path):
            result.append(path[:])  # add current subset
            for i in range(start, len(nums)):
                # skip duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return result
