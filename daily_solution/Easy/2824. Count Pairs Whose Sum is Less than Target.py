class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        result = set()

        # collect all index pairs
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                result.add((i, j))

        count = 0

        # check sums
        for num in result:
            if (nums[num[0]] + nums[num[1]]) < target:
                count += 1
        return count
