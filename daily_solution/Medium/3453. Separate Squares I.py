from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Step 1: total area
        total_area = sum(l*l for _, _, l in squares)
        target = total_area / 2

        # Step 2: slice each square
        def slice_square(y_bottom, side, h):
            y_top = y_bottom + side
            width = side
            
            if h <= y_bottom:
                return 0, side*side
            elif h >= y_top:
                return side*side, 0
            else:
                below_height = h - y_bottom
                above_height = y_top - h
                return width * below_height, width * above_height

        # Step 3: compute total below/above for a given h
        def total_below(squares, h):
            below = 0
            for _, y, l in squares:
                b, _ = slice_square(y, l, h)
                below += b
            return below

        # Step 4: binary search with fixed iterations
        lo = min(y for _, y, _ in squares)
        hi = max(y+l for _, y, l in squares)
        ans = hi
        for _ in range(70):  # fixed iterations, avoids TLE
            mid = (lo + hi) / 2
            below = total_below(squares, mid)
            if below >= target:
                ans = mid
                hi = mid
            else:
                lo = mid
        return round(ans, 5)
