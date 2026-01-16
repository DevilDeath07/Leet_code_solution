class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Step 1: sort to handle duplicates
        results = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                results.append(path[:])  # found a valid combination
                return
            if remaining < 0:
                return

            prev = None
            for i in range(start, len(candidates)):
                # Step 3: skip duplicates at the same depth
                if candidates[i] == prev:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return results
