import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;


/**
 * BEE1068
 */
public class BEE1068 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Deque <String> abre = new ArrayDeque<>();
        Deque <String> fecha = new ArrayDeque<>();
        String frase = entrada.nextLine();
        
        for(int i = 0; i < frase.length(); i++) {
            if (frase.charAt(i) == ')') {
                fecha.push(frase.charAt(i ) + "");
            } 
            if (frase.charAt(i) == '(') {
                abre.push(frase.charAt(i) + "");
            }
        }

        while (abre.size() != 0 && fecha.size() != 0) {
            abre.pop();
            fecha.pop();
        }
        if (abre.size() == 0 && fecha.size() == 0) {
            System.out.println("correct");
        } else {
            System.out.println("incorrect");
        }
        entrada.close();
    }
}