
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
        int king = Integer.parseInt(str[0]);
        int queen = Integer.parseInt(str[1]);
        int rook = Integer.parseInt(str[2]);
        int bishop = Integer.parseInt(str[3]);
        int knight = Integer.parseInt(str[4]);
        int pawn = Integer.parseInt(str[5]);

        int need_king = 1 - king;
        int need_queen = 1 - queen;
        int need_rook = 2 - rook;
        int need_bishop = 2 - bishop;
        int need_knight = 2 - knight;
        int need_pawn = 8 - pawn;

        bw.write(need_king + " " +need_queen + " " +need_rook + " " +need_bishop + " " +need_knight + " " +need_pawn + " " );
        bw.flush();
        bw.close();
        br.close();
    }
}
