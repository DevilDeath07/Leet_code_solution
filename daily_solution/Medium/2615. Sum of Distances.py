from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        groups = defaultdict(list)

        # Step 1: collect indices for each value
        for i, val in enumerate(nums):
            groups[val].append(i)

        # Step 2: compute distances within each group
        for indices in groups.values():
            prefix = [0]
            for idx in indices:
                prefix.append(prefix[-1] + idx)

            total = prefix[-1]
            m = len(indices)

            for k, idx in enumerate(indices):
                left = k * idx - prefix[k]
                right = (total - prefix[k+1]) - (m - k - 1) * idx
                result[idx] = left + right

        return result
