import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int M = s.nextInt();
        int[] moneyPlan = new int[N];
        for (int i = 0; i < N; i++) {
            moneyPlan[i] = s.nextInt();
        }
        System.out.println(solution(N, M, moneyPlan));
    }

    static int solution(int N, int M, int[] moneyPlan) {
        int left = 0;
        int right = 0;
        for (int money : moneyPlan) {
            left = Math.max(left, money);  // 최소 금액은 하루 최대 지출
            right += money;                // 최대 금액은 전체 합
        }

        int answer = right;

        while (left <= right) {
            int mid = (left + right) / 2;

            int cnt = 1;   // 첫 인출
            int sum = 0;

            for (int money : moneyPlan) {
                if (sum + money > mid) { // mid로 커버 불가 → 인출 1회 추가
                    cnt++;
                    sum = money;
                } else {
                    sum += money;
                }
            }

            if (cnt <= M) { // 인출 횟수가 조건 이하라면 더 작은 금액으로 시도
                answer = mid;
                right = mid - 1;
            } else {         // 인출 횟수가 너무 많다면 금액을 늘림
                left = mid + 1;
            }
        }

        return answer;
    }
}
