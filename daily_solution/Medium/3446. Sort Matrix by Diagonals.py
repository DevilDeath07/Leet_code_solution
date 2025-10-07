class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        diag_map = {}

        # Collect elements by diagonal key (i - j)
        for i in range(m):
            for j in range(n):
                key = i - j
                diag_map.setdefault(key, []).append(grid[i][j])

        # Sort each diagonal based on region
        for key in diag_map:
            if key >= 0:  # bottom-left triangle
                diag_map[key].sort(reverse=True)
            else:         # top-right triangle
                diag_map[key].sort()

        # Reconstruct the matrix
        for i in range(m):
            for j in range(n):
                key = i - j
                grid[i][j] = diag_map[key].pop(0)

        return grid
