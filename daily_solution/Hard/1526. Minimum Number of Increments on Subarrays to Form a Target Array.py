class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        count = target[0]

        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                count += target[i] - target[i - 1]
        return count
