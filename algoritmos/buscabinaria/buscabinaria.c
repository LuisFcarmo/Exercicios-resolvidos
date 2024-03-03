#include <stdio.h>

int binary_shearch(int *vetor, int comeco, int fim, int buscando) {
    if (comeco <= fim) {
        int meio = (comeco+fim)/2;
        int chute = vetor[meio];
        if (chute == buscando) return meio;
        else if (chute > buscando) {
            fim = meio-1;
            binary_shearch(vetor, comeco, fim, buscando);
        }
        else {
            comeco = meio+1;
            binary_shearch(vetor, comeco, fim, buscando);
        }
    } else {
        return -1;
    }

}

int main () {
    int vetor[20];
    for (int i = 0; i < 20; i++) {
        vetor[i] = i;
    }
    printf("%d", binary_shearch(vetor, 0, 20, 20));


    return 0;
}