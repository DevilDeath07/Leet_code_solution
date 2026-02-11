class Solution {
    public String reverseWords(String s) {
        String result = "";
		int start = 0;
		for(int i=0 ; i<s.length();i++) {
			if(s.charAt(i)==' ') {
				String temp = s.substring(start,i);
				start = i+1;
				String rev = new StringBuilder(temp).reverse().toString();
				result = result + rev + ' ';	
			}
		}
		String last = new StringBuilder(s.substring(start,s.length())).reverse().toString();
		return result + last;
    }
}
