class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #length of the given array is stored in n
        n=len(nums)
        result=[]
        for i in range(0,n,1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    result=[i,j]
                    break;

        return result
