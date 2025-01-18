class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        min_cost = [[inf]*n for _ in range(m)]
        min_cost[0][0] = 0
        que = deque([(0, 0)])
        while que:
            i, j = que.popleft()
            if i == m-1 and j == n-1:
                return min_cost[i][j]
            for d, ii, jj in (1, i, j+1), (2, i, j-1), (3, i+1, j), (4, i-1, j):
                new_cost = min_cost[i][j] + (grid[i][j] != d)
                if 0 <= ii < m and 0 <= jj < n and new_cost < min_cost[ii][jj]:
                    if d == grid[i][j]:
                        que.appendleft((ii, jj))
                    else:
                        que.append((ii, jj))
                    min_cost[ii][jj] = new_cost
        return -1    
