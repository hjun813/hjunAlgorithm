
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
        String[] str = br.readLine().split(" ");

        int H = Integer.parseInt(str[0]);
        int N = Integer.parseInt(str[1]);

        N = N - 45;
        if(N >= 0){
            System.out.println(H + " " + N);
        }
        else{
            H = H - 1;
            N = N + 60;
            if(H < 0){
                H = H + 24;
            }
            System.out.println(H + " " + N);
        }
    }
}
