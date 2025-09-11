class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        t = sorted([char for char in s if char in vowels])
        result = []
        n = 0
        for char in s:
            if char in vowels:
                result.append(t[n])
                n += 1
            else:
                result.append(char)
        return "".join(result)
