import java.util.Scanner;
import java.util.Stack;
public class ReverseWord {

    public  static void main(String[] args) {
        Stack <Character> teste = new Stack<>();
        Scanner scanf = new Scanner(System.in);
        Integer x;
        String frase;
        Character a;
        x = scanf.nextInt();
        scanf.nextLine();  // Consumir a nova linha após nextInt()

        for (int i = 0; i < x; i++) {
            frase = scanf.nextLine();
            for (int k = 0; k < frase.length(); k++) {
                teste.push(frase.charAt(k));
            }

            while(!teste.isEmpty()) {
                a = teste.pop();
                System.out.print(a);               
            }
        }

        scanf.close();
    }
}


