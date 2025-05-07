class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Edge case: empty list
        
        index = 0  # Pointer for unique values
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:  # Found a unique element
                index += 1
                nums[index] = nums[i]  # Move unique element forward
        
        return index + 1  # Unique count
