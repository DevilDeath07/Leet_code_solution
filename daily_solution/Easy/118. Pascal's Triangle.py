class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        #assume the n value is given rowIndex+1 and doing loop
        for i in range(numRows):
            #create new row list
            row = [1] * (i+1)
            for j in range(1,i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            #append the row list in triangle list
            triangle.append(row)
        
        return triangle
