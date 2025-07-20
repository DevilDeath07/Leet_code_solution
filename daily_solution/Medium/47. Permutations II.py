import itertools
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        unique_perms = set(itertools.permutations(nums))
        tuple_list = list(unique_perms)
        list_of_lists = [list(tup) for tup in tuple_list]
        return list_of_lists
