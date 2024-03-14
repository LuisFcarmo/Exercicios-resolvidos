import java.math.BigInteger;
import java.util.Scanner;

public class AddBinary {
    public static String addBinary(String a, String b) {
        return (new BigInteger(a, 2).add(new BigInteger(b, 2)).toString(2));
    }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println(addBinary(entrada.nextLine(), entrada.nextLine()));
        entrada.close();
    }
}
