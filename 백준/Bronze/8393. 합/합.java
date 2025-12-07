
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split(" ");
        
        int num = Integer.parseInt(str[0]);
        int total = 0;

        for(int i =0; i<=num; i++){ 
            total += i;
        }

        System.out.println(total);
    }
}
