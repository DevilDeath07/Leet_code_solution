class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result = set()
        for num in nums:
            result.add(num)
            reversed_num = int(str(num)[::-1])
            result.add(reversed_num)
        return len(result)
