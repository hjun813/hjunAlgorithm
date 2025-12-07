
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int cnt = 0;

        for(int i = 0; i < N; i++){
            String str[] = br.readLine().split("");

            ArrayList<String> check = new ArrayList<>(); 
            String before = str[0];
            check.add(before);
            int flag = 0;

            for(int a = 1; a < str.length; a++){

                if(!str[a].equals(before)){
                    if(check.contains(str[a])){
                        flag = 1;
                        break;
                    }
                    check.add(str[a]);
                    before = str[a];
                }
                if(flag == 1){
                    break;
                }
            

            }

            if(flag == 0){
                cnt = cnt + 1;
            }


        }
        bw.write(cnt + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}
