import numpy as np

class Solution:
    def numMagicSquaresInside(self, grid):
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        sub_matrices = np.lib.stride_tricks.sliding_window_view(grid, (3, 3))
        count = 0
        
        for i in range(sub_matrices.shape[0]):
            for j in range(sub_matrices.shape[1]):
                m = sub_matrices[i, j]
                
                # Must contain digits 1–9 exactly once
                if set(m.flatten()) != set(range(1, 10)):
                    continue
                
                # Check sums
                if (all(m.sum(axis=1) == 15) and
                    all(m.sum(axis=0) == 15) and
                    m.trace() == 15 and
                    np.fliplr(m).trace() == 15):
                    count += 1
        
        return count
