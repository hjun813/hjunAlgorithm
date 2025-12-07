import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int rest[] = new int[42];
        int ans = 0;

        for(int a = 0; a < 10; a++){
            int x = Integer.parseInt(br.readLine());
            int n = x % 42;
            rest[n] = rest[n] + 1; 
        }

        for(int a = 0; a<42; a++){
            if(rest[a] != 0){
                ans = ans+1;
            }
        }   

        bw.write(ans + "\n");
        bw.flush();
        bw.close();
        br.close();

    }
}
