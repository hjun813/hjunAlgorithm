class Solution {
    public String solution(int[] food) {
        String answer = "0";
        for(int i = food.length-1; i > 0; i--){
            int tmp = (int)(food[i] / 2);
            String add = "";
            for(int j = 0; j < tmp; j++ ){
                add += i;
            }
            answer =  add + answer + add;     
        }
        return answer;
    }
}