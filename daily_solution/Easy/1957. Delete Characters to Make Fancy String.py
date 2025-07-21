class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ''
        for char in s:
            if len(result) < 2 or result[-2:] != char * 2:
                result += char
        return result
