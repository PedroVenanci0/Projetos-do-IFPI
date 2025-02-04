#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TEMPO_MAX 3
#define TAMANHO_MAX 5

typedef struct {
    int dados[TAMANHO_MAX];
    int inicio;
    int fim;
    int tamanho;
} Fila;


Fila* criaFila() {
    Fila* F = (Fila*)malloc(sizeof(Fila));
    F->inicio = 0;
    F->fim = 0;
    F->tamanho = 0;
    return F;
}


bool vazia(Fila* F) {
    return F->tamanho == 0;
}


bool cheia(Fila* F) {
    return F->tamanho == TAMANHO_MAX;
}


void enfileira(int x, Fila* F) {
    if (cheia(F)) {
        printf("Fila cheia!\n");
        return;
    }
    F->dados[F->fim] = x; // Coloca o novo elemento x na posição indicada por fim
    F->fim = (F->fim + 1) % TAMANHO_MAX; // Move o índice fim para a próxima posição
    F->tamanho++;
}

int desenfileira(Fila* F) {
    if (vazia(F)) {
        printf("Fila vazia!\n");
        return -1;
    }
    int valor = F->dados[F->inicio];
    F->inicio = (F->inicio + 1) % TAMANHO_MAX; 
    F->tamanho--;
    return valor;
}

void destroi(Fila* F) {
    free(F);
}

int main(void) {
    Fila* F = criaFila();

    enfileira(67, F); 
    enfileira(85, F); 
    enfileira(93, F); 
    enfileira(16, F); 

    printf("===== Escalonamento Round-Robin =====\n\n");

    while (!vazia(F)) {
        int x = desenfileira(F);
        int t = x / 10; 
        int p = x % 10;  

        printf("Processo %d | Tempo restante: %d\n", p, t);

        if (t > TEMPO_MAX) {
            printf("- Executado por %d unidades de tempo.\n", TEMPO_MAX);
            printf("- Processo %d pausado e reinserido com %d unidades restantes.\n\n", p, t - TEMPO_MAX);
            enfileira((t - TEMPO_MAX) * 10 + p, F);  
        } else {
            printf("- Executado por %d unidades de tempo.\n", t);
            printf("- Processo %d concluído com sucesso.\n\n", p);
        }
    }

    printf("===== Fim da Execução =====\n");

    destroi(F);
    return 0;
}