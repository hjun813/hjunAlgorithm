
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        String str[] = br.readLine().split(" ");
        int num[] = new int[N];
        for(int i = 0; i<N; i++){
            num[i] = Integer.parseInt(str[i]);
        }
        int cnt = 0;
        int v = Integer.parseInt(br.readLine());
        for(int j = 0; j<N; j++){
            if(num[j] == v){
                cnt = cnt + 1;
            }
        }
        
        bw.write((cnt)+"\n");
        bw.flush();
        bw.close();
        br.close();
        


    }
}
