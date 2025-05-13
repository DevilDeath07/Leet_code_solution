class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #the values in nums array the loop repeated then it will remove the element in the array
        while val in nums:
            #using arr.remove(value) function
            nums.remove(val)
          #return the len of the array
        return len(nums)
