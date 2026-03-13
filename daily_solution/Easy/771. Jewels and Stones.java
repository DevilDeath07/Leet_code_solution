import java.util.*;
class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        HashSet<Character> table = new HashSet<>();
        for (char ch : jewels.toCharArray()) {
            table.add(ch);
        }
        int count = 0;

        for(char ch : stones.toCharArray()){
            if(table.contains(ch)){
                count++;
            }
        }
        return count;
        

    }
}
