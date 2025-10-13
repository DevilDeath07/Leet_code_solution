from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        for i in range(1, len(words)):
            if not (Counter(words[i].lower()) == Counter(result[-1].lower())):
                result.append(words[i])
        return result
