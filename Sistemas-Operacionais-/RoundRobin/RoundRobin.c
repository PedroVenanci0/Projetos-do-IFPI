#include <stdio.h>

typedef struct {
    int id;
    int tempo_execucao;
    int tempo_restante;
    int tempo_chegada;
    int tempo_termino;
} Processo;

void round_robin(Processo processos[], int num_processos, int quantum, int troca_contexto) {
    int tempo_total = 0, processos_restantes = num_processos;
    int tempo_vida[num_processos], tempo_espera[num_processos];

    // Inicializa os tempos de vida e de espera para 0
    for (int i = 0; i < num_processos; i++) {
        tempo_vida[i] = 0;
        tempo_espera[i] = 0;
        processos[i].tempo_restante = processos[i].tempo_execucao; // Inicializa o tempo restante
    }

    while (processos_restantes > 0) {
        int progresso = 0; // Para saber se algum processo foi executado
        for (int i = 0; i < num_processos; i++) {
            if (processos[i].tempo_restante > 0 && processos[i].tempo_chegada <= tempo_total) {
                int tempo_executado = (processos[i].tempo_restante > quantum) ? quantum : processos[i].tempo_restante;
                tempo_total += tempo_executado;
                processos[i].tempo_restante -= tempo_executado;

                // Se o processo terminou, registra o tempo de término
                if (processos[i].tempo_restante == 0) {
                    processos[i].tempo_termino = tempo_total;
                    tempo_vida[i] = processos[i].tempo_termino - processos[i].tempo_chegada;
                    tempo_espera[i] = tempo_vida[i] - processos[i].tempo_execucao;
                    processos_restantes--;
                } else {
                    // Se o processo ainda não terminou, realiza troca de contexto
                    tempo_total += troca_contexto;
                }

                progresso = 1; // Indica que um processo foi executado
            }
        }

        // Se nenhum processo foi executado em um ciclo, incrementa o tempo_total
        if (!progresso) {
            tempo_total++;
        }
    }

    // Calculando as médias de tempo de vida e tempo de espera
    int soma_tempo_vida = 0, soma_tempo_espera = 0;
    for (int i = 0; i < num_processos; i++) {
        soma_tempo_vida += tempo_vida[i];
        soma_tempo_espera += tempo_espera[i];
    }

    float tempo_medio_vida = (float)soma_tempo_vida / num_processos;
    float tempo_medio_espera = (float)soma_tempo_espera / num_processos;

    printf("Tm_vida = %.0f u.t\n", tempo_medio_vida);
    printf("Tm_espera = %.0f u.t\n", tempo_medio_espera);
}

int main() {
    Processo processos[] = {
        {1, 10, 10, 5, 0},  
        {2, 30, 30, 15, 0}, 
        {3, 20, 20, 10, 0}, 
        {4, 40, 40, 0, 0}   
    };

    int num_processos = sizeof(processos) / sizeof(processos[0]);
    int quantum = 15;
    int troca_contexto = 4;

    round_robin(processos, num_processos, quantum, troca_contexto);

    return 0;
}
