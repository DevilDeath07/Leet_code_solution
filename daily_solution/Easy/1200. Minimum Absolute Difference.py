class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        n = len(arr)

        # find the minimum absolute difference
        min_diff = min(arr[i+1] - arr[i] for i in range(n-1))

        # Step 2: Collect pairs with that min_diff
        result = []
        for i in range(n - 1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i], arr[i+1]])
        return result
