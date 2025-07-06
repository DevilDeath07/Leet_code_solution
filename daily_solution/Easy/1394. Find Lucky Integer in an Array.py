class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        lucky_numbers = [num for num, freq in counter.items() if num == freq]
        if len(lucky_numbers) != 0:
            return max(lucky_numbers)
        else:
            return -1
