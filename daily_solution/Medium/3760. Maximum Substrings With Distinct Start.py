class Solution:
    def maxDistinct(self, s: str) -> int:
        #find number of distinct element in the given string. We can create a that much number of distinct starting substring 
          are also created
        return len(set(s))
