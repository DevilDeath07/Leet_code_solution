class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = [pref[0]]
        temp = 0
        for i in range(1,len(pref)):
            temp = pref[i-1] ^ pref[i]
            result.append(temp)
        return result

        
