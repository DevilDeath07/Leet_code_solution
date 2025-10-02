class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        totalDrunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            totalDrunk += 1
            empty -= numExchange - 1
            numExchange += 1  # Increment AFTER using current rate

        return totalDrunk
