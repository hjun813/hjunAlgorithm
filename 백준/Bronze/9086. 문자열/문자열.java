
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int T = Integer.parseInt(br.readLine());

        for(int a = 0; a < T; a++){
            String str[] = br.readLine().split("");
            int l = str.length;
            bw.write(str[0] + str[l-1] + "\n");
            
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
