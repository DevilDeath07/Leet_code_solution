##java solution
class Solution {
        
    public static String searchOccurrence(String[] arr, String key) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals(key)) {
                count++;
            }
        }
        if (count == 1) {
            return key;
        }
        return null;
    }
    public String[] uncommonFromSentences(String s1, String s2) {
        String total = s1 + " " + s2;
        String[] words = total.split(" ");
        List<String> last = new ArrayList<>();
        for (String word : words) {
            String result = searchOccurrence(words, word);
            if (result != null) {
            	last.add(result);
            }
        }
        String[] arr = last.toArray(new String[0]);
        return arr;
    }
}

----------------------(or)------------------------------------------

#python
from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sa = s1 + " " + s2
        s = sa.split()
        counter = Counter(s)
        result = []
        for ele, fre in counter.items():
            if fre==1:
                result.append(ele)
        return result
