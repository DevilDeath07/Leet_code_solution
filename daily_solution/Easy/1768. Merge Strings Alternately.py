class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        min_len = min(len(word1), len(word2))

        # Merge alternately up to the length of the shorter word
        for i in range(min_len):
            result += word1[i] + word2[i]

        # Append the remaining part of the longer word
        if len(word1) > len(word2):
            result += word1[min_len:]
        else:
            result += word2[min_len:]

        return result
