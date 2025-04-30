class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            digits = []
            while nums[i] > 0:
                digits.append(nums[i] % 10)
                nums[i] = nums[i] // 10
            if len(digits)%2==0:
                count +=1
        return count
