class Solution {
    public int solution(int n, int w, int num) {
        int answer = 1; 
        int num1 = num % (2*w);
       
        if(num1 != 1 && num1 != 0)
        {for(int i = num + 1; i <= n; i++){
            if((i % (2*w)) == num1 || (i % (2*w)) == 2*w + 1 - num1){
 
                answer += 1;
            }
        }}
        else{
            for(int i = num + 1; i <= n; i++){
            if((i % (2*w)) == 1 || (i % (2*w)) == 0){
                answer += 1;
            }
        }
        }
        
        return answer;
    }
}