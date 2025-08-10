class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_count = sorted(str(n))
        for i in range(31):
            temp = sorted(str(1<<i))
            if n_count == temp:
                return True
        return False

