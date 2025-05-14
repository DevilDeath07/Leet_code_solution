class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1 = s.upper()
        temp2 = t.upper()

        if sorted(temp1) == sorted(temp2):
            return True
        return False
