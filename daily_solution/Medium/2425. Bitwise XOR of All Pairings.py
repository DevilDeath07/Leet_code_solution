class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        i=j=0
        if len(nums1)%2:
            for x in nums2:
                i^=x
        if len(nums2)%2:
            for x in nums1:
                j^=x   
        return i^j
