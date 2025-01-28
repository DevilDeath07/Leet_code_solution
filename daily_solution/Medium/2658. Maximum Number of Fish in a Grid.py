class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r=len(grid)
        c=len(grid[0])
        visited=[[False]*c for _ in range(r)]
        direction=[(0,1),(0,-1),(1,0),(-1,0)]

        def calculate_Max_fish(a,b):
            if a<0 or a>=r or b<0 or b>=c or visited[a][b] or grid[a][b]==0:
                return 0
            visited[a][b] = True
            count = grid[a][b]
            for d_a,d_b in direction:
                count+=calculate_Max_fish(a+d_a,b+d_b)
            return count


        result=0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    continue
                elif grid[i][j]>0:
                    result = max(result,calculate_Max_fish(i,j))
        
        return result
