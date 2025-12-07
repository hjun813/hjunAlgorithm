
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        int test = Integer.parseInt(str);

        // switch (test) {
        //     case : 
                
        //         break;
        //     default:
        //         throw new AssertionError();
        // }
        if(90<=test && test<=100){
            System.out.println("A");
        }
        else if (80<=test && test<90) {
            System.out.println("B");
        }
        else if (70<=test && test<80) {
            System.out.println("C");
        }
        else if (60<=test && test<70) {
            System.out.println("D");
        }
        else{
            System.out.println("F");
        }
    }
}
