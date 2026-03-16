import java.util.*;

class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        ArrayList<Integer> less = new ArrayList<>();
        ArrayList<Integer> equal = new ArrayList<>();
        ArrayList<Integer> greater = new ArrayList<>();

        for(int i: nums){
            if(i == pivot){
                equal.add(i);
            }
            if(i < pivot){
                less.add(i);
            }
            if(i > pivot){
                greater.add(i);
            }
        }
        // Merge all three lists into one
        ArrayList<Integer> merged = new ArrayList<>();
        merged.addAll(less);
        merged.addAll(equal);
        merged.addAll(greater);

        // Convert to int[]
        int[] arr = merged.stream().mapToInt(Integer::intValue).toArray();
        return arr;
    }
}
