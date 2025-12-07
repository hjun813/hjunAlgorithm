
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        String[] str = br.readLine().split(" ");
        int num[] = new int[N];

        for(int i = 0; i<N; i++){
            num[i] = Integer.parseInt(str[i]);
        }
        // System.out.println((Math.min(num)));
        // System.out.println((Math.max(num)));
        int min = num[0];
        int max = num[0];

        for (int i = 1; i < N; i++) {
            if (num[i] < min) min = num[i];
            if (num[i] > max) max = num[i];
        }

        bw.write(min + " " + max);
        bw.newLine();
        bw.flush();
        bw.close();
        br.close();
    }
}
