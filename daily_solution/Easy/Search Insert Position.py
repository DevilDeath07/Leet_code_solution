class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # If target is not in nums, insert it and sort the list
        if target not in nums:
            nums.append(target)
            nums.sort() 
        # Return the index of target
        return nums.index(target)
        
