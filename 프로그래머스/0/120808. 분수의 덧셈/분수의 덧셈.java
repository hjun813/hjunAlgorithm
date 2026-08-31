class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        // 1. 두 분수를 통분하여 더하기
        int numer = (numer1 * denom2) + (numer2 * denom1);
        int denom = denom1 * denom2;
        
        // 2. 분자와 분모의 최대공약수(GCD) 구하기
        int gcdValue = getGcd(numer, denom);
        
        // 3. 분자와 분모를 최대공약수로 나누어 기약 분수 만들기
        return new int[] { numer / gcdValue, denom / gcdValue };
    }
    
    // 유클리드 호제법을 이용한 최대공약수 계산 메서드
    private int getGcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}