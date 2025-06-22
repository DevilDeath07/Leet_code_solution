from collections import Counter

class Solution:
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        count = 0
        for i in counter.values():
            if i>1 and Solution.is_prime(i):
                count += 1
        if count == 0:
            return False
        else:
            return True
