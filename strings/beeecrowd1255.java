package beecrowd.strings;

import java.util.Scanner;

public class beeecrowd1255 {
    public class freq_letters {
        char x;
        int qtd;
    }
    freq_letters[] vet_freq = new freq_letters[26];

    static void frequency_letters (String x) {
        for (int i = 0; i < x.length(); i++) {
            for (int k = 0; k < x.length(); k++) {
                if (x.charAt(i) == x.charAt(i)) {

                }
            }
        }
        return;
    }

    public static void main(String[] args) {
        int qtd = 0;
        Scanner entry = new Scanner(System.in);
        String text;
        qtd = entry.nextInt();
        while (qtd != 0) {  
            text = entry.nextLine();
            frequency_letters(text);
         
                
        
            qtd--;
        }   

        entry.close();
    }
}
