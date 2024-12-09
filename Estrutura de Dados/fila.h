#ifndef FILA_H
#define FILA_H

#include <stdio.h>
#include <stdlib.h>

// Tipo de itens armazenados na fila (pode ser alterado conforme a necessidade)
typedef char Itemf;

// Estrutura da fila
typedef struct fila {
    int max;      // Capacidade máxima da fila
    int total;    // Total de elementos na fila
    int inicio;   // Índice do início da fila
    int final;    // Índice do final da fila
    Itemf *item;  // Vetor dinâmico para armazenar os itens
} *Fila;

// Macro para calcular o índice circular
#define avanca(i, F) (((i) + 1) % (F)->max)

// Inicializa uma nova fila com capacidade `m`
Fila fila(int m);

// Verifica se a fila está vazia
int vaziaf(Fila F);

// Verifica se a fila está cheia
int cheiaf(Fila F);

// Insere um item na fila
void enfileira(Itemf x, Fila F);

// Remove um item da fila
Itemf desenfileira(Fila F);

// Libera a memória alocada para a fila
void destroi(Fila *G);

#endif
