class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        #check the square is magic or not
        def is_magic_square(square: List[List[int]]) -> bool:
            n = len(square)
            if n == 0:
                return False

            # Sum of the first row as reference
            target_sum = sum(square[0])

            # Check all rows
            for row in square:
                if sum(row) != target_sum:
                    return False

            # Check all columns
            for col in range(n):
                if sum(square[row][col] for row in range(n)) != target_sum:
                    return False

            # Check main diagonal
            if sum(square[i][i] for i in range(n)) != target_sum:
                return False

            # Check secondary diagonal
            if sum(square[i][n - 1 - i] for i in range(n)) != target_sum:
                return False

            return True
        #find all possible magic square by using given grid
        def find_magic_squares(matrix: List[List[int]]) -> List[Tuple[Tuple[int, int], List[List[int]]]]:

            rows, cols = len(grid), len(grid[0])
            results = []

            # Try all possible square sizes
            for size in range(1, min(rows, cols) + 1):  # allow 1x1, 2x2, etc.
                for i in range(rows - size + 1):
                    for j in range(cols - size + 1):
                        square = [grid[i+k][j:j+size] for k in range(size)]
                        if is_magic_square(square):
                            results.append(square)

            return results

        #call the functions
        square = find_magic_squares(grid)
        count = 0
        for element in square:
            count = max(count, len(element))
        return count
