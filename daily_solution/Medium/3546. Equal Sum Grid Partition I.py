import numpy as np
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        matrix = np.array(grid)

        # --- Vertical split (rows) ---
        for i in range(1, len(grid)):  # try splitting after each row
            top = np.sum(matrix[:i, :])
            bottom = np.sum(matrix[i:, :])
            if top == bottom:
                return True

        # --- Horizontal split (columns) ---
        for j in range(1, len(grid[0])):  # try splitting after each column
            left = np.sum(matrix[:, :j])
            right = np.sum(matrix[:, j:])
            if left == right:
                return True

        return False
