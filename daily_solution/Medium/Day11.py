class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        char_counts = {}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1

        odd_count = 0
        for count in char_counts.values():
            if count % 2 != 0:
                odd_count += 1

        return odd_count <= k
