class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result = float('inf')
        for i in range(len(nums)):
            temp = 0
            if nums[i] == target:
                temp = abs(i - start)
                result = min(temp,result)
        return result
        
