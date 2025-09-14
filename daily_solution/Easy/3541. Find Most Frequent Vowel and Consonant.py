from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'aeiou'
        count = Counter(s)
        max_vowel = 0
        max_consonant = 0

        for char, freq in count.items():
            if char in vowels:
                max_vowel = max(max_vowel, freq)
            else:
                max_consonant = max(max_consonant, freq)
        return max_vowel+max_consonant
