import java.util.Scanner;

public class beecrowd1182 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int total = 0;
        int valor = 0;
        int coluna_e = entrada.nextInt();
        entrada.nextLine();
        String opera = entrada.nextLine();

        for (int coluna = 0; coluna < 12; coluna++) {
            for (int linha = 0; linha < 12; linha++) {
                valor = entrada.nextInt();
                entrada.nextLine();
                if (coluna == coluna_e) {
                    total += valor;
                } 
            }
        }

        if (opera.equals("S")) {
            System.out.printf("soma = %d", total);
        } else {
            System.out.printf("media = %d", total/12);
        }
        entrada.close();
    }
}
