package l2;

import java.util.Scanner;

public class q2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int anterior = 0;
        int[] vetor = new int[11];
        boolean ordenado = true;
        int crescente = 0;
        int descescente = 0;
        int x = 0;

        for (int i = 0; i < 10; i++) {
            vetor[i] = entrada.nextInt();

            if (vetor[i] - anterior > 2) {
                ordenado = false;
            }

            if (vetor[i] - anterior == 1) {
                crescente++;
            }

            if (vetor[i] - anterior == -1) {
                descescente++;
            }
            entrada.nextLine();

            anterior = vetor[i];
        }

        x = entrada.nextInt();
        entrada.nextLine();
        int qtd = 0;

        for (int i = 0; i < 10; i++) {
            if (vetor[i] == x) {
                qtd++;
            }
        }

        System.out.println("apareceu = " + qtd);
        System.out.println("ordenado = " + ordenado);
        if (crescente == 10) {
            System.out.println("crescente = " + true);
        }
        if (descescente == 10) {
            System.out.println("decrescente = " + false);
        }

        entrada.close();
    }
}
