#include "fila.h"

// Inicializa uma nova fila com capacidade `m`
Fila fila(int m) {
    Fila F = malloc(sizeof(struct fila));
    if (F == NULL) {
        printf("Erro: Falha ao alocar memória para a fila.\n");
        exit(1);
    }
    F->max = m;
    F->total = 0;
    F->inicio = 0;
    F->final = 0;
    F->item = malloc(m * sizeof(Itemf));
    if (F->item == NULL) {
        printf("Erro: Falha ao alocar memória para os itens da fila.\n");
        free(F);
        exit(1);
    }
    return F;
}

// Verifica se a fila está vazia
int vaziaf(Fila F) {
    return F->total == 0;
}

// Verifica se a fila está cheia
int cheiaf(Fila F) {
    return F->total == F->max;
}

// Insere um item na fila
void enfileira(Itemf x, Fila F) {
    if (cheiaf(F)) {
        printf("Erro: Fila cheia!\n");
        return;
    }
    F->item[F->final] = x;
    F->final = avanca(F->final, F);
    F->total++;
}

// Remove um item da fila
Itemf desenfileira(Fila F) {
    if (vaziaf(F)) {
        printf("Erro: Fila vazia!\n");
        exit(1);
    }
    Itemf x = F->item[F->inicio];
    F->inicio = avanca(F->inicio, F);
    F->total--;
    return x;
}

// Libera a memória alocada para a fila
void destroi(Fila *G) {
    if (G == NULL || *G == NULL) return;
    if ((*G)->item != NULL) {
        free((*G)->item);
        (*G)->item = NULL;
    }
    free(*G);
    *G = NULL;
}
