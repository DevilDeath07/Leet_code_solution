import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        m = len(potions)

        for spell in spells:
            min_required = (success + spell - 1) // spell  
            idx = bisect.bisect_left(potions, min_required)
            result.append(m - idx)
        return result
