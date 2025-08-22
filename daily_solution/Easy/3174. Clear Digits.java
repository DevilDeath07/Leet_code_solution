class Solution {
    public String clearDigits(String s) {
        ArrayList<Character> st = new ArrayList<>();
		for (int i = 0; i < s.length(); i++) {
		    char ch = s.charAt(i);
		    
		    if (!Character.isDigit(ch)) {
		        st.add(ch);
		    }
		    if (Character.isDigit(ch)){
		    	st.remove(st.size() - 1);
		    }
        }
        StringBuilder sb = new StringBuilder();
        for (char ch : st) {
            sb.append(ch);
        }
        return sb.toString();
    }
}
