class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #the given string is empty it return empty
        if not strs:
            return ""
        #sort the stings array
        strs.sort()
        #firststring is 
        first_str = strs[0]
        #last string is
        last_str = strs[-1]
        #initialize i value
        i = 0
        #check the length of the first string and last string less than i
        # first string [i] is equal to last string[i]
        #we increment i = i +1
        while i < len(first_str) and i<len(last_str) and first_str[i] == last_str[i]:
            i +=1
        #return the first string [:i]
        return first_str[:i]
        
