class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            temp = [i for i in range(len(nums)) if target == nums[i]]
            return [temp[0],temp[len(temp)-1]]
        
        return [-1,-1]
