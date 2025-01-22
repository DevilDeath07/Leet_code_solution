class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row=len(isWater)
        col=len(isWater[0])
        height=[[float('inf')]* col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if isWater[i][j]==1:
                    height[i][j]=0
                else:
                    if i>0:
                        height[i][j]=min(height[i][j],height[i-1][j]+1)
                    if j>0:
                        height[i][j]=min(height[i][j],height[i][j-1]+1)
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if i<row-1:
                    height[i][j]=min(height[i][j],height[i+1][j]+1)
                if j<col-1:
                    height[i][j]=min(height[i][j],height[i][j+1]+1)
        return height
