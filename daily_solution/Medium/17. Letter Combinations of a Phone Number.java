import java.util.*;

class Solution {
    public List<String> letterCombinations(String digits) {
        Map<Character, String> table = new HashMap<>();

        table.put('2', "abc");
        table.put('3',"def");
        table.put('4',"ghi");
        table.put('5',"jkl");
        table.put('6',"mno");
        table.put('7',"pqrs");
        table.put('8',"tuv");
        table.put('9',"wxyz"); 

        //based on the given integer to take the combinations
        List<String> result = new ArrayList<String>();
        if (digits == null || digits.length() == 0) return result;
        backtrack(result, new StringBuilder(), digits, 0, table);
        return result;
    }

    private void backtrack(List<String> result, StringBuilder current, String digits, int index, Map<Character, String> table) {
        if (index == digits.length()) {
            result.add(current.toString());
            return;
        }

        String letters = table.get(digits.charAt(index));
        for (char c : letters.toCharArray()) {
            current.append(c);
            backtrack(result, current, digits, index + 1, table);
            current.deleteCharAt(current.length() - 1); // backtrack
        }
    }
}
