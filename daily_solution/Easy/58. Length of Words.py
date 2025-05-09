class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the string into words
        words = s.split()
        # Check if there are any words in the string
        if not words:
            return 0
        # Get the last word
        last_word = words[-1]
        # Return the length of the last word
        return len(last_word)
