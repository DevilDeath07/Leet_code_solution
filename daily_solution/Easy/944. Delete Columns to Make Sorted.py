from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        r = len(strs)
        c = len(strs[0])
        count = 0
        grid = []

        # Build each column string
        for j in range(c):          # loop over columns
            temp = ""
            for i in range(r):      # loop over rows
                temp += strs[i][j]  
            grid.append(temp)

        # Check if each column string is sorted
        for word in grid:
            if word != ''.join(sorted(word)):
                count += 1
        return count
