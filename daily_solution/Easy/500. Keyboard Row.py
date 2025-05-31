class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        result = []
        n = len(words)
        for i in range(n):
            lower_word = set(words[i].lower())
            if lower_word.issubset(first_row) or lower_word.issubset(second_row) or lower_word.issubset(third_row):
                result.append(words[i])

        return result
