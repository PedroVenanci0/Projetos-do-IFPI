// Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos

import { question } from "readline-sync";

console.log ('Calculando Horario total')

// Entrada

var tempo_min = Number (question('Qual o tempo em minutos:'))

// processamento

const tempo_hrs = (tempo_min / 60)


// saida

console.log (`o horario total equivale a ${tempo_hrs} hrs`)

