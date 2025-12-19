class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return Solution().fib(n-1)+Solution().fib(n-2)
