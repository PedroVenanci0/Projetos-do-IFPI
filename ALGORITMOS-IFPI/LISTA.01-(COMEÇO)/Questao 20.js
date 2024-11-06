// 20. Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)

import { question } from "readline-sync"

console.log ('conversor de temperatura de celsius para Farenheits')

// Entrada 

var celsius = Number(question('Informe a temperatura em celsius: '))

// Processamento

const Farenheits = ((9 * celsius + 160) / 5).toFixed(2)

// Saida 

console.log (`A conversão de temperatura para Farenheits é de ${Farenheits} graus `)