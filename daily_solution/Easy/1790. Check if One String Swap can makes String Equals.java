class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        //declear and define two temp variable and the value is -1
        int temp1=-1;
        int temp2=-1;
      //decleare the swap_count variable
        int swap_count=0;
      //Start the loop where the end of the loop in length of stiring either s1 and s2
        for (int i=0;i<s1.length();i++){
            if (s1.charAt(i)!=s2.charAt(i)){
                swap_count+=1;
                if (temp1==-1)
                    temp1=i;
                else if (temp2==-1)
                    temp2=i;
            }
        }
      //swap count==0 the given strings is same
        if (swap_count==0)
            return true;
        if (swap_count==2 && s1.charAt(temp1)==s2.charAt(temp2) && s1.charAt(temp2)==s2.charAt(temp1))
            return true;
      //otherwise False and not equals
        return false;
        
    }
}
