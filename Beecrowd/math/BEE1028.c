#include <stdio.h>

int trivial_mdc(int a, int b) {
    int divisor;
    if (a == b) return a;
    if (a < b) {
        for (int i = 1; i <= a; i++) {
            if ((a % i == 0) && (b % i == 0)) {
                divisor = i;
            }
        }
    }
    if (b < a) {
        for (int i = 1; i <= b; i++) {
            if ((a % i == 0) && (b % i == 0)) {
                divisor = i;
            }
        }
    }
    return divisor;
}
int main () {
    int qtd;
    int valor1 = 0, valor2 = 0;
    scanf("%d", &qtd);
    while (qtd--) {
        scanf("%d %d%*c", &valor1, &valor2);
        printf("%d\n", trivial_mdc(valor1, valor2));
    }
    
}