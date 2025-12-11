from typing import List
from collections import defaultdict
import bisect

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row = defaultdict(list)
        col = defaultdict(list)

        # Group by row and column
        for x, y in buildings:
            row[y].append(x)
            col[x].append(y)

        # Sort once
        for v in row.values():
            v.sort()
        for v in col.values():
            v.sort()

        covered = 0

        for x, y in buildings:
            xs = row[y]
            ys = col[x]

            xi = bisect.bisect_left(xs, x)
            yi = bisect.bisect_left(ys, y)

            if xi > 0 and xi < len(xs) - 1 and yi > 0 and yi < len(ys) - 1:
                covered += 1

        return covered
