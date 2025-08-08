import math
class Solution:
    def soupServings(self, n: int) -> float:
        m = math.ceil(n/25)
        if m > 500:
            return 1.0
        else:
            from functools import lru_cache

            # Step 2: Define recursive function with memoization
            @lru_cache(None)
            def dp(i, j):
                # Base cases
                if i <= 0 and j <= 0:  # both empty
                    return 0.5
                if i <= 0:  # A empty first
                    return 1.0
                if j <= 0:  # B empty first
                    return 0.0

                # Step 3: Average over the four serving options
                return (
                    dp(i - 4, j) +
                    dp(i - 3, j - 1) +
                    dp(i - 2, j - 2) +
                    dp(i - 1, j - 3)
                ) / 4
            return dp(m,m)
