class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        def dfs(r, c, island_id):
            if 0 <= r < n and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = island_id
                return 1 + dfs(r + 1, c, island_id) + dfs(r - 1, c, island_id) + dfs(r, c + 1, island_id) + dfs(r, c - 1, island_id)
            return 0

        island_sizes = {0: 0}
        island_id = 2
        max_island = 0

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, island_id)
                    island_sizes[island_id] = size
                    max_island = max(max_island, size)
                    island_id += 1

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighbor_islands = set()
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != 0:
                            neighbor_islands.add(grid[nr][nc])

                    max_island = max(max_island, 1 + sum(island_sizes[i] for i in neighbor_islands))

        return max_island
