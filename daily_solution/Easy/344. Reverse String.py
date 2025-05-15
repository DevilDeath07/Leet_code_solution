class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        result = ''.join(s) #convert into one string
        temp = result[::-1] # reverse the string
        s[:] = [*temp] #then convert into list and store in given list
