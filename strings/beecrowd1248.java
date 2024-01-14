package beecrowd.strings;

import java.util.Scanner;

public class beecrowd1248 {
    public static int alitera(String x) {
        String[] repartida = x.split(" ");
        int qtd = 0;
        for (int i = 0; i < repartida.length-1; i++) {
            if (repartida[i].toLowerCase().charAt(0) == repartida[i+1].toLowerCase().charAt(0)){
                qtd++;
            } else {
            }
        }
        
        return qtd;   
    }
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String texto = new String();
        texto = entrada.nextLine();
        while ((texto != null)) {
            System.out.printf("%d", alitera(texto));
            texto = entrada.nextLine();
        }   
        entrada.close();
    }
}
