import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int minimumCost(int[] nums) {
        int n = nums.length; 
        int ans = Integer.MAX_VALUE;  
        for (int i = 1; i < n - 1; i++) { 
            for (int j = i + 1; j < n; j++) {           
                int sum = nums[0] + nums[i] + nums[j]; 
                ans = Math.min(ans, sum); 
            } 
        } 
        return ans;
    }
}
