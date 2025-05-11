class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #count the values
        count = Counter(nums)
        
        for num in nums:
            if count[num]>1:
                return True
        return False
        
