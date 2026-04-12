from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Map each value to its list of indices
        positions = defaultdict(list)
        for i, val in enumerate(nums):
            positions[val].append(i)
        
        result = float('inf')
        
        # For each value, check all consecutive triplets of indices
        for indices in positions.values():
            if len(indices) >= 3:
                for j in range(len(indices) - 2):
                    a, b, c = indices[j], indices[j+1], indices[j+2]
                    temp = abs(a - b) + abs(b - c) + abs(c - a)
                    result = min(result, temp)
        
        return -1 if result == float('inf') else result

-----------------------------------java----------------------------------------------

import java.util.*;
class Solution {
    public int minimumDistance(int[] nums) {
         HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();

        // Step 1: store indexes
        for (int i = 0; i < nums.length; i++) {
            map.putIfAbsent(nums[i], new ArrayList<>());
            map.get(nums[i]).add(i);
        }

        int result = Integer.MAX_VALUE;

        // Step 2: check ALL triples
        for (ArrayList<Integer> group : map.values()) {

            if (group.size() >= 3) {

                for (int i = 0; i <= group.size() - 3; i++) {

                    int a = group.get(i);
                    int b = group.get(i + 1);
                    int c = group.get(i + 2);

                    int temp = Math.abs(a - b)
                             + Math.abs(b - c)
                             + Math.abs(c - a);

                    result = Math.min(result, temp);
                }
            }
        }

        // Step 3: Output
        if (result == Integer.MAX_VALUE) {
            return -1;
        } else {
            return result;
        }
    }
}
