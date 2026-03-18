import java.util.*;
class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        Hashtable<Integer, String> table = new Hashtable<>();
        int n = names.length;
        for(int i = 0; i < n;i++){
            table.put(heights[i],names[i]);
        }
        Arrays.sort(heights);
        
        String[] result = new String[n];
    
        for(int i= 0; i < n;i++){
            result[i] = table.get(heights[i]);
        }
        Collections.reverse(Arrays.asList(result));

        return result;
    }
}
