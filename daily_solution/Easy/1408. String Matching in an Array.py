class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substring=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    substring.append(words[i])
        substring = list(set(substring))
        return substring
