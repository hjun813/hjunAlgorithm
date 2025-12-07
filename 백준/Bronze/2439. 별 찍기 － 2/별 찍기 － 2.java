import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split(" ");

        int N = Integer.parseInt(str[0]);

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N-i-1; j++){
                System.out.print(" ");
            }
            for (int j = N-i-1; j<N; j++){
                System.out.print("*");
            }
            System.out.println();
        }

    }
}
