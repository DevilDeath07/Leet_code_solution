class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result_set = set()
        current_ors = set()

        for num in arr:
            current_ors = {num | x for x in current_ors} | {num}
            result_set |= current_ors

        return len(result_set)
