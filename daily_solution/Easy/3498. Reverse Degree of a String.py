class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet_dict = {chr(i): 26 - (i - 97) for i in range(97, 123)}
        count = 0
        for i in range(len(s)):
            count += (i+1)*alphabet_dict[f'{s[i]}']
        return count
