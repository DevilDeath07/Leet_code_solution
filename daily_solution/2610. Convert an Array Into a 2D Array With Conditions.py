from collections import defaultdict
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # dictionary to track how many times each number has appeared
        freq = defaultdict(int)

        result = []
        for num in nums:
            # place each occurrence of num into the correct subarray
            if freq[num] >= len(result):
                result.append([])
            result[freq[num]].append(num)
            freq[num] += 1

        return result
