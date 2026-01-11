class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for ele in matrix:
            if target in ele:
                return True
        return False
