class Solution:
    def doesAliceWin(self, s: str) -> bool:
            vowels = "aeiouAEIOU"
            return False if(sum([1 for char in s if char in vowels]) == 0) else True
