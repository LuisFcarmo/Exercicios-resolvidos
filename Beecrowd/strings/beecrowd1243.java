package beecrowd.strings;

import java.util.Scanner;

public class beecrowd1243 {
    public static void main(String[] args) {
        Scanner entry = new Scanner(System.in);
        int size = 0;
        int qtd = 0;
        String text = entry.nextLine();
        String []split_vector = text.split(" ");
        for (int i = 0; i < split_vector.length; i++) {
            if (!(split_vector[i].matches("."))){
                if(split_vector[i].toUpperCase().matches("[A-Z]*")){
                    size += split_vector[i].length();
                    qtd++;
                }
            }
        }
        if (qtd > 0) {    
            qtd = size/qtd;
        }
        if (qtd <= 3) {
            System.out.println(250);
        }
        else if (qtd > 3 && qtd <= 5) {
            System.out.println(500);
        }
        else {
            System.out.println(1000);
        }
        entry.close();
    }
}
