package q2;

import java.util.Scanner;

public class loteriateste {
    public static void main(String[] args) {
        loteria x = new loteria();
        Scanner entrada = new Scanner(System.in);
        int tentativas = 0;
        int chute = 0;
        while(true) {
            tentativas++;
            chute = entrada.nextInt();
            entrada.nextLine();
            switch (x.chutar(chute)) {
                case 1:
                    System.out.println("numero maior");
                    break;
                case 2:
                    System.out.println("numero menor");
                    break;
                default:    
                    System.out.println("acertou");
                    break;
            }       
            if(x.chutar(chute) == 3) {
                break;
            }
        }
        System.out.println("numeros de tentativas " + tentativas);

        entrada.close();
    }
}
