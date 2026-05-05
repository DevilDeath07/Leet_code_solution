from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        result = []

        # Place characters in the order specified
        for ch in order:
            result.append(ch * count[ch])
            count[ch] = 0

        # Add remaining characters not in order
        for ch, freq in count.items():
            if freq > 0:
                result.append(ch * freq)

        return "".join(result)
