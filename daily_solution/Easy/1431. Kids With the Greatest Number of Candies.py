class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy_have = max(candies)
        result = []
        for candy in candies:
            result.append(candy+extraCandies >= max_candy_have)
        return result
