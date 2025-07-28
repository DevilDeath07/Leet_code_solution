class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        from itertools import chain, combinations

        def find_subsets(arr):
            return list(chain.from_iterable(combinations(arr, r) for r in range(len(arr) + 1)))

        def find_bitwise(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
            result = 0
            for num in arr:
                result |= num
            return result

        sorted_nums = sorted(nums)

        subsets = [list(subset) for subset in find_subsets(sorted_nums)]

        max_sub_bitwise = find_bitwise(sorted_nums)
        answer = 0

        for i in range(len(subsets)):
            if find_bitwise(subsets[i]) == max_sub_bitwise:
                answer +=1

        return answer
