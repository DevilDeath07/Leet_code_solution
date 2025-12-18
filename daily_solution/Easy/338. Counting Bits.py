class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            binary = f"{i:b}"
            result.append(binary.count("1"))
        return result
