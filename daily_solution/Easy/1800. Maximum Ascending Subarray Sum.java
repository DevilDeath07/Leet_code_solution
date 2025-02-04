class Solution {
    public int maxAscendingSum(int[] nums) {
        //length of nums array are stored in length
        int length=nums.length;
        int max_subarray_sum=0;
        //start loop for creating subarray
        for(int start=0;start<length;start++){
            int subarray_sum=nums[start];
            int end=start+1;
            //start another while loop for sum of subarray 
            while(end<length && nums[end]>nums[end-1]){
                subarray_sum+=nums[end];
                end+=1;
            }
            //use Math.max buit-in function for find maximum subaray sum
            max_subarray_sum=Math.max(max_subarray_sum,subarray_sum);
        }
        //return the maximum subarray sum 
        return max_subarray_sum;
        
    }
}
