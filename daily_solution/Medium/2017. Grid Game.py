class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        down, right = 0, sum(grid[0])        
        outcomes = []
        for i in range(len(grid[0])):
            right -= grid[0][i]
            outcomes.append(max(down, right))
            down += grid[1][i]
        return min(outcomes)
