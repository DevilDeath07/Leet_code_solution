import java.util.*;
class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i: nums){
            map.put(i, map.getOrDefault(i,0)+1);
        }

        int max1 = 0, ele1 = 0;
        int max2 = 0, ele2 = 0;
        for(Map.Entry<Integer, Integer> entry : map.entrySet() ){
            int key = entry.getKey();
            int value = entry.getValue();

            if (value > max1){
                max2 = max1;
                ele2 = ele1;
                max1 = value;
                ele1 = key;
            }
            else if(value > max2){
                max2 = value;
                ele2 = key;
            }

        }
        int[] result = {ele1, ele2};
        return result;
    }
}
