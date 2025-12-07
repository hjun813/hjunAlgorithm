
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str[] = br.readLine().split(" ");

        int N = Integer.parseInt(str[0]);
        int M = Integer.parseInt(str[1]);

        int ball[] = new int[N];
        for(int a=0; a<N; a++){
            ball[a] = a+1;
        }


        for(int a = 0; a<M; a++){
            String changeinfo[] = br.readLine().split(" ");
            int i = Integer.parseInt(changeinfo[0]);
            int j = Integer.parseInt(changeinfo[1]);

            int temp = ball[i-1];
            ball[i-1] = ball[j-1];
            ball[j-1] = temp;
        }

        for(int a = 0; a<N; a++){
            bw.write(ball[a] + " ");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
