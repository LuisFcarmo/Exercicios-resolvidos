#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

int main () {
    node *stack = NULL;
    node *removido = NULL;
    node *aux = NULL;
    int qtd;
    int elemento_removido;

    while(scanf("%d", &qtd) != 0) {
        for (int i = qtd; i >= 1; i--) {
            push(&stack, i);
        }
        int int_aux;
        
        while (qtd > 1) {
            elemento_removido = get_top(&stack);
            push(&removido, elemento_removido);
            pop(&stack);
            int_aux = get_top(&stack);
            adicionar_comeco(&stack, int_aux);
            pop(&stack);

            qtd--;
            aux = stack;
        }
        aux = removido;
        printf("pilha dos removidos :(");
        while (aux != NULL) {
            printf("%d ", aux -> valor);
            aux = aux -> prox;
        }
        aux = stack;
        printf(")\nSobrou na pilha :");
        printf("%d", aux -> valor);
        aux = NULL;

        esvaziar_pilha(&removido);
        esvaziar_pilha(&stack);
        removido = NULL;
        stack = NULL;
    }
        
    
    return 0;
}