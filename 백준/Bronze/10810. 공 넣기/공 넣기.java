
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str[] = br.readLine().split(" ");

        int N = Integer.parseInt(str[0]);
        int M = Integer.parseInt(str[1]);

        int ball[] = new int[N]; 

        for(int a = 0; a < M; a++){
            String ballinfo[] = br.readLine().split(" ");
            int i = Integer.parseInt(ballinfo[0]);
            int j = Integer.parseInt(ballinfo[1]);
            int k = Integer.parseInt(ballinfo[2]);
            
            for(int b = i; b < j+1; b++){
                ball[b-1] = k;
            }

        }
        for(int c = 0; c < N; c++){
            bw.write(ball[c] + " ");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
