class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power=3
        result = [(power**i) for i in range(0,31)]
        if n in result:
            return True
        else:
            return False
