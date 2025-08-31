class Solution {
    public int differenceOfSums(int n, int m) {
        int num1 = 0;
        int num2 = 0;
        List<Integer> list = new ArrayList<>();
        for(int i=1; i<=n;i++){
            list.add(i);
        }
        for(int num: list){
            if (num%m == 0){
                num2 +=num;
            }
            else{
                num1 += num;
            }
        }
        return num1 - num2;
    }
}
