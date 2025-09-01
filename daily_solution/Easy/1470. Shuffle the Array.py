class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 = nums[:n]
        arr2 = nums[n:]
        result = []
        for i in range(n):
            result.append(arr1[i])
            result.append(arr2[i])
        return result
