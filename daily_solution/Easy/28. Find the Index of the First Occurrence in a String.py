class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #The given neddle string in haystack then
        #give the postition of the starting index in the haystack string
        if needle in haystack:
            return haystack.find(needle)#using haystack.find() to find position
        return -1
