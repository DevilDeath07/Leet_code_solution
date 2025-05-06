class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #find the length of nums array of n distinct number
        n = len(nums)
        #doing loop for the n distinct number in the nums array check
        #if there exist continue otherwise return the missing number
        for i in range(0,n+1):
            if i in nums:
                continue
            else:
                return i
        
