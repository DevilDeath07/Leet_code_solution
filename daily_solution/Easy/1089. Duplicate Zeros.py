class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                # Insert a zero at i+1 and drop the last element
                arr.insert(i+1, 0)
                arr.pop()
                i += 2  # skip over the duplicated zero
            else:
                i += 1
