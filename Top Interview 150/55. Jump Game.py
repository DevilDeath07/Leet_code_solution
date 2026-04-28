class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)):
            if i > count:
                    return False
                
            count = max(count, i + nums[i])
        return True
