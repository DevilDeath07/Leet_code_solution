class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #length of the list
        n = len(nums)
        #calculate the no of element divided by 2
        regex = n/2
        #using counted to count each element can repeated how many times
        count = Counter(nums)
        #iterate
        for i in nums:
            #counter[i] is greater than the calculate value then print the value
            if count[i]>=regex:
                return i
        #otherwise return -1
        return -1       
