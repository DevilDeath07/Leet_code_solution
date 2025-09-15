class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        String[] words = text.split("\\s+");
        char[] chars = brokenLetters.toCharArray();
        int count = 0;
        for (String word : words) {
            for (char c : chars) {
                if (word.contains(String.valueOf(c))) {
                    count += 1;
                    break;
                }
            }
        }

        int result = words.length - count;
        return result;
    }
}
