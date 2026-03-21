import numpy as np

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        # --- Extract submatrix ---
        flip = []
        for row in range(x, x + k):       # only k rows
            temp = []
            for col in range(y, y + k):   # only k cols
                temp.append(grid[row][col])
            flip.append(temp)
        # --- Flip vertically ---
        matrix = np.array(flip)
        flipped_matrix = np.flip(matrix, axis=0)

        # --- Write back into grid ---
        for row in range(x, x + k):
            for col in range(y, y + k):
                grid[row][col] = int(flipped_matrix[row - x][col - y])
        return grid
