// Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

import { question } from "readline-sync"

console.log ('Conversor de horas para minutos')

// Entrada 

var tempo_min = Number (question('Qual o valor em minutos:'))

var tempo_hrs = Number (question('Qual o valor em horas:'))

// processamento 

const tempo_total = (tempo_hrs * 60) + tempo_min

//saida

console.log (`valor total em minutos é ${tempo_total}`)