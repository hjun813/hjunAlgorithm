
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] str = br.readLine().split(" ");
        int X = Integer.parseInt(str[0]);
        int N = Integer.parseInt(br.readLine());
        
        for(int i = 0; i < N; i++){
            String[] str2 = br.readLine().split(" ");
            int m = Integer.parseInt(str2[0]);
            int n = Integer.parseInt(str2[1]);
            X = X - m*n;
        }
        if(X == 0){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }

    }
}
