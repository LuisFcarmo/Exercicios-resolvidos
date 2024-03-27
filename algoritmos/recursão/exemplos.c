#include <stdio.h>
void printar(int max) {
    static int x = 1;
    if (max == x)
        return;
    printf("%d", x);
    x++;
    printar(max);
}

int fat(int num) {
    if (num == 1)
        return 1;
    else
    {
        return num * fat(num - 1);
    }
}

int size(int vet[4]) {
    static int x;
    if (x != 4) {
        x++;
        size(vet);
    }
    else {
        return x;
    }
}


int main()
{
    // printar(19);
    int vet[4] = {1, 2, 3, 9};
    // printf("%d", fat(5));
    // 4.1 Escreva o código para a função soma, vista anteriormente.

    // 4.2 Escreva uma função recursiva que conte o número de itens em uma lista.
    //  printf("%d", size(vet));

    // 4.3 Encontre o valor mais alto em uma lista.
    printf("%d", maior(vet));

    return 0;
}