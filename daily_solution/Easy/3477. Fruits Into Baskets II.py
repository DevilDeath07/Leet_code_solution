class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False] * len(baskets)  # Track basket usage
        perfect = 0

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if not used[j] and fruits[i] <= baskets[j]:
                    used[j] = True
                    perfect += 1
                    break
                else:
                    continue

        result = len(fruits) - perfect
        return result
