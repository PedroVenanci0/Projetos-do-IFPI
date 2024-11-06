// 21. Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).

import { question } from "readline-sync"

console.log ('conversor de temperatura de Farenheits para celsius ')

// Entrada 

var Farenheits = Number(question('Informe a temperatura em Farenheits: '))

// Processamento

const celsius = ((5 * Farenheits - 160) / 9).toFixed(2)

// Saida 

console.log (`A temperatura em celsius é de ${celsius} graus `)



