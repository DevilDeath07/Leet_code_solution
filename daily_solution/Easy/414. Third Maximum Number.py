class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums), reverse=True)
        if len(unique_nums)>=3:
            return unique_nums[2]
        else:
            return unique_nums[0]
