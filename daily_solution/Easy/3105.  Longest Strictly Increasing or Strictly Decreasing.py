class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        max_length=0
        for i in range(n):
            count=1
            for j in range(i+1,n):
                if nums[j]>nums[j-1]:
                    count+=1
                else:
                    break
            max_length=max(max_length,count)

            count=1
            for j in range(i+1,n):
                if nums[j]<nums[j-1]:
                    count+=1
                else:
                    break
            max_length=max(max_length,count)
        return max_length
         
