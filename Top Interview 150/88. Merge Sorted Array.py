class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = nums1[:m] + nums2[:n]
        merged.sort()

        # Copy back into nums1 in-place
        for i in range(m + n):
            nums1[i] = merged[i]
