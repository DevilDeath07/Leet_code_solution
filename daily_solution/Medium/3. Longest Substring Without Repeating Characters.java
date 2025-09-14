import java.util.HashSet;
import java.util.Set;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max = 0;
        int n = s.length();
        for(int i =0 ; i<n ; i++){
            Set<Character> set = new HashSet<>();
            for(int j = i; j<n; j++){
                if (set.contains(s.charAt(j))) {
                    break;
                }
                set.add(s.charAt(j));
                max = Math.max(max, j - i + 1);
            }
        }
        return max;
    }
}
