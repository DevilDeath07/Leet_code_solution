class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #sort the array
        sorted_array = sorted(nums)
        #count occurance of each element
        count = Counter(sorted_array)
        #iterate i in sorted_array
        for i in sorted_array:
            #count[i] == 1:
            #return i
            if count[i] ==1:
                return i
        return -1

       

        
