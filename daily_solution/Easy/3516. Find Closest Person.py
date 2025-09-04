class Solution {
    public int findClosest(int x, int y, int z) {
        int p1top3 = Math.abs(x-z);
        int p2top3 = Math.abs(y-z);
        if(p1top3<p2top3){
            return 1;
        }
        else if(p1top3>p2top3){
            return 2;
        }
        else{
            return 0;
        }
    }
}
