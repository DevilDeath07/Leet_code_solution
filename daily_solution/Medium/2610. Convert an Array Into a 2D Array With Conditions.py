class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        placed = defaultdict(int)
        result = []

        for num in nums:
            row_index = placed[num]
            if row_index == len(result):
                result.append([])
            result[row_index].append(num)
            placed[num] += 1

        return result
