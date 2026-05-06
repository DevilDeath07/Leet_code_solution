class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        #rotate the given list
        rotate = [list(row) for row in zip(*boxGrid[::-1])]

        #write the function for falling stones
        def fall_stones(box):
            rows, cols = len(box), len(box[0])

            for col in range(cols):
                # Start from bottom row upwards
                empty_row = rows - 1
                for row in range(rows - 1, -1, -1):
                    if box[row][col] == '*':
                        # Reset empty_row above obstacle
                        empty_row = row - 1
                    elif box[row][col] == '#':
                        # Move stone down if possible
                        if row != empty_row:
                            box[empty_row][col] = '#'
                            box[row][col] = '.'
                        empty_row -= 1
                    # If '.', just continue
            return box

        #call the function
        result = fall_stones(rotate)
        return result
