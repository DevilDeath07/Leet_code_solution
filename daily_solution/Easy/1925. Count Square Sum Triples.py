import itertools
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0

        for a in range(1, n+1):
            for b in range(1, n+1):
                c2 = a*a + b*b
                c = int(c2**0.5)
                if c <= n and c*c == c2 and c not in (a,b):
                    count += 1
        return count
