class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n=len(words)
        string1=None
        string2=None
        count=0
        for i in range(n):    
            for j in range(i+1,n):
                string1=words[i]
                string2=words[j]
                if len(string1)>len(string2):
                    continue
                if (isPrefixAndSuffix(string1, string2)==True):
                   count+=1
        return count
def isPrefixAndSuffix(str1,str2):
    s1=str2.startswith(str1)
    s2=str2.endswith(str1)
    return s1 and s2
   
