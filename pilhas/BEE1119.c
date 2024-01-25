#include <stdio.h>
#include <stdlib.h>

void swap(int *vetor, int elemento1, int elemento2) {
    int aux = vetor[elemento1];
    vetor[elemento1] = vetor[elemento2];
    vetor[elemento2] = aux;
    return;
}

int particionar(int *vetor, int left, int right, char c) {
    int pivo;

    if (c == 'c') {
        pivo = vetor[left];
    } else {
        pivo = vetor[right];
        swap(vetor, left, right);  
    }

    int i = left + 1;

    for (int k = left + 1; k <= right; k++) {
        if ((c == 'c' && vetor[k] <= pivo) || (c != 'c' && vetor[k] >= pivo)) {
            swap(vetor, i, k);
            i++;
        }
    }

    swap(vetor, left, i - 1); 
    return i - 1;
}


void quicksort(int *vetor, int left, int right, char c) {
    if (left < right) {
        int indice_pivot = particionar(vetor, left, right, c);
        quicksort(vetor, left, indice_pivot-1, c);
        quicksort(vetor, indice_pivot+1, right, c);
    }
}

int main () {
    int qtd;
    int valor;
    scanf("%d", &qtd);
    int o = 0, p = 0;
    int *par = (int*) calloc(sizeof(int), qtd);
    int *impar = (int*) calloc(sizeof(int), qtd);

    for (int  i = 0; i < qtd; i++) {
        scanf("%d%*c", &valor);
        if(valor%2 == 0) {
            par[o] = valor;
            o++;
        } else {
            impar[p] = valor;
            p++;
        }
    }
    quicksort(par, 0, o, 'c');
    quicksort(impar, 0, p, 'd');
    printf("pares ");
    for (int i = 0; i < o; i++) {
        printf("%d ", par[i]);
    }
    printf("\n");
    printf("impares ");
    for(int i = 0; i < p; i++) {
        printf("%d ", impar[i]);
    }

    return 0;
}