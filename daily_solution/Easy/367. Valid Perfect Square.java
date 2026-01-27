class Solution {
    public boolean isPerfectSquare(int num) {
        double result = Math.floor(Math.sqrt(num));
        if(num == (result*result)){
            return true;
        }
        return false;

    }
}
