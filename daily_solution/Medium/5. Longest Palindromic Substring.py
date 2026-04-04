class Solution:
    def longestPalindrome(self, s: str) -> str:
        substrings = []
        length = len(s)

        # Generate substrings using start and end indices
        for start in range(length):
            for end in range(start + 1, length + 1):
                temp = s[start:end]
                if temp == temp[::-1]:   # check palindrome
                    substrings.append(temp)

        result = ""
        for ch in substrings:
            if len(result) < len(ch):
                result = ch
        return result
