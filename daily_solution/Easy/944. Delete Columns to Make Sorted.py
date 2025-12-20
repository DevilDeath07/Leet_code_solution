class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        r = len(strs)
        c = len(strs[0])
        count = 0

        # Check each column
        for col in range(c):
            for row in range(1, r):
                if strs[row][col] < strs[row-1][col]:
                    count += 1
                    break   # No need to check further in this column
        return count
