import java.util.Scanner;

public class beecrowd1183 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int total = 0;
        int valor = 0;
        String opera = entrada.nextLine();

        for (int linha = 0; linha < 4; linha++) {
            for (int coluna = 0; coluna < 4; coluna++) {
                valor = entrada.nextInt();
                entrada.nextLine();
                if (coluna > linha) {
                    total += valor;
               }
            }
        }

        if (opera.equals("S")) {
            System.out.printf("soma = %d", total);
        } else {
            System.out.printf("media = %d", total/66);
        }
        entrada.close();
    }
}
