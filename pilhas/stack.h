#ifndef _stack
#define _stack

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct _node {
    struct _node *prox;
    int valor;
} node;

node *criar_no (int valor) {
    node *novo_no = (node*) malloc(sizeof(node)*1);
    novo_no -> prox = NULL;
    novo_no -> valor = valor;
    return novo_no;
}

void push (node **stack, int valor) {
    node *novo_no = criar_no(valor);

    if (*stack == NULL) {
        *stack = novo_no;
    } else {
        node *atual = *stack;
        while (atual -> prox != NULL) {
            atual = atual -> prox;
        }
        atual -> prox = novo_no;
    }
}

int tamanho_pilha (node **stack) {
    node *ref = *stack;
    int i = 0;
    while (ref != NULL) {
        i++;
        ref = ref -> prox;
    }
    return i;
}

int get_top (node **stack) {
    node *ref = *stack;
    while (ref -> prox != NULL) {
        ref= ref -> prox;
    }
    return ref -> valor;
}

void pop (node **stack) {
    node* atual = *stack;
    while (atual -> prox -> prox != NULL) {
        atual = atual -> prox;
    }   
    free (atual -> prox);
    atual -> prox = NULL;
}

void adicionar_comeco (node **stack, int valor) {
    node *novo_no = criar_no(valor);
    node *ref = *stack;
    *stack = novo_no;
    (*stack) -> prox = ref;
}

void esvaziar_pilha(node **stack) {
    node *begin = *stack;
    node *aux = NULL;
    while (begin != NULL) {
        aux = begin;
        begin = begin -> prox;
        free(aux);
    }
}

#endif
