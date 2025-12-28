class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        #find the row and coloumn length based on the given grid array

        row = len(grid[0])
        col = len(grid)
        count = 0

        #perform search for count the negative numbers in the given array

        for i in range(col):
            for j in range(row):
                if grid[i][j]<0:
                    count +=1
        return count
