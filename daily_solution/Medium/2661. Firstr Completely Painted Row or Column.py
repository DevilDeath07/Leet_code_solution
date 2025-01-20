import numpy as np
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        inv = np.argsort(arr)
        M = np.vectorize(lambda x: inv[x-1])(mat)

        return int(min(M.max(axis=0).min(), M.max(axis=1).min()))
