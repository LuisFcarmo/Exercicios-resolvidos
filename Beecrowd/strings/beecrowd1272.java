package beecrowd.strings;

import java.util.Scanner;

public class beecrowd1272 {
    public static void main(String[] args) {
        int qtd;
        Scanner entry = new Scanner(System.in);
        qtd = entry.nextInt();
        entry.nextLine();

        while (qtd > 0) {
            String text = entry.nextLine();
            String[] split_text = text.split(" ");
            String Ocult_message = "";
            
            for (String word: split_text) {
                Ocult_message = Ocult_message.concat(word.substring(0, 1));
            }
            
            System.out.println(Ocult_message);
            qtd--;   
        }
        entry.close();
    }
}
