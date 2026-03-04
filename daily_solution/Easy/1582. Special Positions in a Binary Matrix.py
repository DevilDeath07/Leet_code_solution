class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row = sum(mat[i])
                    col = sum(mat[k][j] for k in range(m))
                    if row == 1 and col ==1:
                        count +=1
        return count
