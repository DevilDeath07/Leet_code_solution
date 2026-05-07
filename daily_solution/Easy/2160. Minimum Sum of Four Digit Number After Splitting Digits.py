class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(str(num))
        # Build two numbers by alternating digits
        new1 = int(digits[0] + digits[2])
        new2 = int(digits[1] + digits[3])
        return new1 + new2

  ----------------------------(or)------------------------------------------------

import itertools

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = list(str(num))
        results = set()

        # Permute all digits
        for perm in itertools.permutations(digits, len(digits)):
            s = "".join(perm)
            # Split into two parts at every possible position
            for i in range(1, len(s)):
                first, second = int(s[:i]), int(s[i:])
                results.add((first, second))

        # Find minimum sum
        solution = float('inf')
        for first, second in results:
            solution = min(solution, first + second)

        return solution

