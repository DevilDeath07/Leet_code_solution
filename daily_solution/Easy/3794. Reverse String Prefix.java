#java 
class Solution {
    public String reversePrefix(String s, int k) {
        String temp = s.substring(0,k);
        String rev = new StringBuilder(temp).reverse().toString();
        String result = rev + s.substring(k,s.length());
        return result;
    }
}

------------------------------------------(or)----------------------------------------------

#python
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        split = s[:k]
        result = split[::-1] + s[k:]
        return result
