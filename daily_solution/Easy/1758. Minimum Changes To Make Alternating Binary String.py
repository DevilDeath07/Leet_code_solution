class Solution:
    def minOperations(self, s: str) -> int:
        # Pattern 1: starts with '0' → "010101..."
        flips1 = sum(ch != ('0' if i % 2 == 0 else '1') for i, ch in enumerate(s))
        # Pattern 2: starts with '1' → "101010..."
        flips2 = sum(ch != ('1' if i % 2 == 0 else '0') for i, ch in enumerate(s))
        return min(flips1, flips2)
