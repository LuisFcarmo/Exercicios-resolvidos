package l1.q1;

public class primo {
    private primo() {
    };

    public static String isPrime(Integer x) {
        int qtd = 0;
        for (int i = 2; i <= x; i++) {
            if (x % i == 0) {
                qtd++;
            }
        }
        if (qtd != 1)
            return "No";
        return "Yes";
    };
}
