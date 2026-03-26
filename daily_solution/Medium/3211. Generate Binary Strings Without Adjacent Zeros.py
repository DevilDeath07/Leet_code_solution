class Solution:
    def validStrings(self, n: int) -> List[str]:
        def has_adjacent_zeros(s: str) -> bool:
            for i in range(len(s) - 1):
                if s[i] == s[i+1] == "0":
                    return True
            return False


        array = []
        for i in range(2**n):
            temp = bin(i)[2:].zfill(n)
            array.append(temp)
            
        result = []
        for word in array:
            if not(has_adjacent_zeros(word)):
                result.append(word)
        
        return result
