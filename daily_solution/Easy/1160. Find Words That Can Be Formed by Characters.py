class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count =0
        char_count = Counter(chars)

        for word in words:
            word_count = Counter(word)
            if all(word_count[c] <= char_count[c] for c in word_count):
                count += len(word)
        return count
