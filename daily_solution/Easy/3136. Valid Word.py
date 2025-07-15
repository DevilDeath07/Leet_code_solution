class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False
        if len(word)>= 3:
            for char in word:
                if not char.isalnum():
                    return False
                if char.isalpha():
                    if char in vowels:
                        has_vowel = True
                    else:
                        has_consonant = True
            return has_vowel and has_consonant
        else:
            return False
        
