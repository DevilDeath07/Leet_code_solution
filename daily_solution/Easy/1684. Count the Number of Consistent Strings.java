import java.util.*;

class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        HashSet<Character> table = new HashSet<>();
        for(char ch: allowed.toCharArray()){
            table.add(ch);
        }
        int count = 0;
        for(String word: words){
            boolean isconsistant = true;
            for (char c : word.toCharArray()) {
                if (!table.contains(c)) {
                    isconsistant = false;
                    break; // Found a disallowed character
                }
            }
            if(isconsistant){
                count++;
            }
        }
        return count;
    }
}
