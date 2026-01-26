import java.util.*;

class Solution {
    public String reverseVowels(String s) {
        // Define vowels
        Set<Character> vowels = new HashSet<>(
            Arrays.asList('a','e','i','o','u','A','E','I','O','U')
        );

        // Collect vowels
        List<Character> vowelsList = new ArrayList<>();
        for (char ch : s.toCharArray()) {
            if (vowels.contains(ch)) {
                vowelsList.add(ch);
            }
        }

        // Reverse vowels
        Collections.reverse(vowelsList);

        // Convert string to char array for mutation
        char[] sArr = s.toCharArray();
        int idx = 0;

        // Replace vowels with reversed ones
        for (int i = 0; i < sArr.length; i++) {
            if (vowels.contains(sArr[i])) {
                sArr[i] = vowelsList.get(idx);
                idx++;
            }
        }

        // Convert back to string
        return new String(sArr);
    }
}
