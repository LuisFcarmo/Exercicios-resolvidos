
import java.util.Scanner;

public class palindrome {
    public static boolean isPalindrome(int x) {
        String y = Integer.toString(x);
        int k = 0;
        int l = y.length() - 1;
        System.out.println(k);
        System.out.println(l);

        for (; k < y.length() - 1 && l >= 0;) {
            k++;
            l--;
            if (y.charAt(k) != y.charAt(l)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        if (isPalindrome(entrada.nextInt())) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }

        entrada.close();
    }
}
