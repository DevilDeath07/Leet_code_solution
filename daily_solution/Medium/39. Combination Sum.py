class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()

        def backtrack(combo, total):
            if total == target:
                result.add(tuple(sorted(combo)))  # Store sorted tuple to avoid duplicates
                return
            if total > target:
                return

            for num in candidates:
                combo.append(num)
                backtrack(combo, total + num)
                combo.pop()

        backtrack([], 0)
        return [list(tup) for tup in result]
