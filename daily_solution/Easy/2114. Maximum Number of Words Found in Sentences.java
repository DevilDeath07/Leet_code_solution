class Solution {
    public int mostWordsFound(String[] sentences) {
        int count = 0;
        for(String s:sentences){
            String[] arr = s.split(" ");
            int temp = arr.length;
            count = Math.max(count,temp);
        }
        return count;
        
    }
}
