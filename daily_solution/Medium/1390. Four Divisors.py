import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        count = 0
        def find_divisors(n):
            divisors = set()
            for i in range(1, int(math.isqrt(n)) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
            return sorted(divisors)
        for num in nums:
            divi = find_divisors(num)
            if len(divi) == 4:
                count += sum(divi)
        return count
