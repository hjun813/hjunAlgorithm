import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // 사람 수
        int M = sc.nextInt(); // 최소 스텟

        sc.nextLine();
        String line = sc.nextLine();
        int[] status = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();

        Arrays.sort(status); // 스텟 정렬
        
        int e = status.length; 
        int cnt = 0;

        if(N == 1){
            System.out.println(0);
        }
        else{
            for(int i = 0; i < e; i++){
                for(int j = e-1; j > i ; j--){
                    // System.out.println("c!" + i + j);
                    // System.out.println("check" + status[i] + status[j]);
                    if(status[i] + status[j] >= M){
                        cnt += 1;
                        // System.out.println("!!" + i + j);
                        e = j;
                        break;
                    }
                    else{
                        break;
                    }
                }
            }
            System.out.println(cnt);
        }
        
    }

    
}
