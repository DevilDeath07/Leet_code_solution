class Solution {
    public int maxAscendingSum(int[] nums) {
        //length of nums array are stored in length
        int length=nums.length;
        int max_subarray_sum=0;
        //start loop
        for(int start=0;start<length;start++){
            int subarray_sum=nums[start];
            int end;
            for(end=start+1;end<length && nums[end]>nums[end-1];end++){
                subarray_sum+=nums[end];
            }
            max_subarray_sum=Math.max(max_subarray_sum,subarray_sum);
        }
        return max_subarray_sum;
        
    }
}
