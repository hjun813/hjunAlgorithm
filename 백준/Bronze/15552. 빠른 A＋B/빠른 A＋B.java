
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String num = br.readLine();

        int T = Integer.parseInt(num);

        for(int i = 0; i<T; i++){
            String[] test = br.readLine().split(" ");
            int A = Integer.parseInt(test[0]);
            int B = Integer.parseInt(test[1]);
            
            bw.write((A+B) + "\n");
        }
        bw.flush();
        bw.close();
        br.close();

    }
}
