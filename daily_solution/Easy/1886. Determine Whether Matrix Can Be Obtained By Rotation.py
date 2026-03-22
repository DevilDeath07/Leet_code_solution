class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            return [list(row) for row in zip(*mat[::-1])]

        current = mat
        for _ in range(4):  # try 0°, 90°, 180°, 270°
            if current == target:
                return True
            current = rotate(current)
        else:
                return False
