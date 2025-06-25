class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        temp = sorted(arr)
        temp1 = sorted(target)
        if temp1 == temp:
            return True
        else:
            return False
