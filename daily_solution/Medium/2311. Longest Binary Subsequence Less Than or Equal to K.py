class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        subsequence = []
        value = 0
        power = 0

        # Traverse from right to left (LSB to MSB)
        for ch in reversed(s):
            if ch == '0':
                subsequence.append('0')  # Always safe to include
            else:
                if power < 32 and value + (1 << power) <= k:
                    value += (1 << power)
                    subsequence.append('1')
            power += 1

        # Reverse to restore original order
        return len(''.join(reversed(subsequence)))
