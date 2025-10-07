class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full, dry, ans = {}, SortedList(), [-1] * len(rains)
        for i, lake in enumerate(rains):
            if lake:
                if lake in full:
                    j = dry.bisect_right(full[lake])
                    if j == len(dry): return []
                    ans[dry.pop(j)] = lake
                full[lake] = i
            else:
                dry.add(i)
                ans[i] = 1
        return ans
