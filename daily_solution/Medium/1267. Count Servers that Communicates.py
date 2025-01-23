class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row=len(grid)
        col=len(grid[0])
        rc=[0]*row
        cc=[0]*col
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    rc[i]+=1
                    cc[j]+=1
        result=0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (rc[i] > 1 or cc[j] > 1):
                    result += 1
        return result
