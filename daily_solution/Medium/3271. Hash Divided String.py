class Solution:
    def stringHash(self, s: str, k: int) -> str:
        # Create dictionary for lowercase alphabets a-z starting at index 0
        alphabet_dictionary = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}

        # Reverse dictionary: index -> character
        reverse_dictionary = {v: k for k, v in alphabet_dictionary.items()}
        result = ""

        # Process string in chunks of size k
        for i in range(0, len(s), k):
            str1 = s[i:i+k]   # safer slicing
            indices = [alphabet_dictionary[ch] for ch in str1]
            hash_val = sum(indices) % 26
            result += reverse_dictionary[hash_val] 
        return result
