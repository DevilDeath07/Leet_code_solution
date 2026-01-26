import java.util.Arrays;
import java.util.ArrayList; 
import java.util.List;

class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int n = arr.length;

        // Find the minimum absolute difference
        int min_diff = Integer.MAX_VALUE;
        for (int i = 0; i < n - 1; i++) {
            int diff = arr[i + 1] - arr[i];  // sorted array ensures non-negative
            if (diff < min_diff) {
                min_diff = diff;
            }
        }

        // Collect pairs with that min_diff
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < n - 1; i++) {
            if (arr[i + 1] - arr[i] == min_diff) {
                result.add(Arrays.asList(arr[i], arr[i + 1]));
            }
        }

        return result;
    }
}
