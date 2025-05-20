class Solution:
    def isHappy(self, n: int, seen=None) -> bool:
        if seen is None:
            seen = set()  # Initialize set for cycle detection

        if n == 1:
            return True
        if n in seen:  # Cycle detected
            return False

        seen.add(n)
        digits = [int(digit) for digit in str(n)]
        temp = sum(d ** 2 for d in digits)

        return self.isHappy(temp, seen)  # Proper recursive call

