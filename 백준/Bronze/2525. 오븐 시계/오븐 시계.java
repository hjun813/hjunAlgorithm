
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split(" ");

        int A = Integer.parseInt(str[0]);
        int B = Integer.parseInt(str[1]);
        int C = Integer.parseInt(br.readLine());

        int h = C / 60;
        int m = C % 60;

        A = A + h;
        B = B + m;
        if(B >= 60){
            A = A + 1;
            B = B - 60;
        }
        if(A >= 24){
            A = A - 24;
        }
        System.out.println(A + " " + B);

    }
}
