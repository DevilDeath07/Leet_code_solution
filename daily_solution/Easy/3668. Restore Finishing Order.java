import java.util.*;

class Solution {
    public int[] recoverOrder(int[] order, int[] friends) {

        Hashtable<Integer, Integer> table = new Hashtable<>();
        ArrayList<Integer> result = new ArrayList<>(friends.length);

        // insert friends into hashtable
        for (int j : friends) {
            table.put(j, j);
        }

        // check order
        for (int j : order) {
            Integer val = table.get(j);

            if (val != null) {
                result.add(val);
            }
        }

        // convert ArrayList to array
        int[] ans = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            ans[i] = result.get(i);
        }

        return ans;
    }
}
