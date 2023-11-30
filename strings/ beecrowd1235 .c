#include <stdio.h>
int len (char *palavra) {
    int i = 0;
    while (palavra[i] != '\0') {
            i++;
        
    }
    return i;
}

int main () {
    char palavra[200];
    int tamanho = 0;
    int qtd = 0;
    scanf("%d%*c", &qtd);
  
    while (qtd--)
    {
        scanf("%[^\n]%*c", palavra);
        tamanho = len(palavra);
        for (int i = (tamanho/2); i >= 0; i--) {
            printf("%c", palavra[i]);
        }
        for (int i = tamanho; i > tamanho/2; i--) {
            printf("%c", palavra[i]);
        }   
    }

    return 0;
}