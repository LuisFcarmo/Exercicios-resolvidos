import java.util.Scanner;

public class beecrowd3076 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Double seculo;
        for (int i = 0; i < 5; i++) {
            seculo = entrada.nextDouble();
            entrada.nextLine();
            seculo = seculo / 100;
            System.out.println(Math.ceil(seculo));
        }
        entrada.close();
    }
}