#include "fila.h" // Inclui as funções e estruturas da fila

#define TEMPO_MAX 3 // Define o tempo máximo de execução de um processo

int main(void) {
    Fila F = fila(5); // Cria uma fila com capacidade 5

    // Adiciona elementos na fila
    enfileira(67, F);
    enfileira(85, F);
    enfileira(93, F);
    enfileira(16, F);

    while (!vaziaf(F)) {
        // Remove o próximo processo
        int x = desenfileira(F);
        int t = x / 10; // Tempo necessário para o processo
        int p = x % 10; // Número do processo

        if (t > TEMPO_MAX) {
            // Reinsere o processo com o tempo restante
            enfileira((t - TEMPO_MAX) * 10 + p, F);
        } else {
            // Finaliza o processo
            printf("Processo %d concluído\n", p);
        }
    }

    destroi(&F); // Libera a memória da fila
    return 0;
}
