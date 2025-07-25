import java.util.HashSet;
import java.util.Set;

class Solution {
    public int maxSum(int[] nums) {
        int maxNum = nums[0];
        for (int num : nums) {
            if (num > maxNum) {
                maxNum = num;
            }
        }
        if (maxNum<0){
            return maxNum;
        }
        else{
            int result = 0;
            Set<Integer> uniqueNums = new HashSet<>(Arrays.asList(
                Arrays.stream(nums).boxed().toArray(Integer[]::new)
            ));
            for(int num : uniqueNums) {
                if (num > 0){
                    result += num;
                }
            }
            return result;
            
        }
    }
}
