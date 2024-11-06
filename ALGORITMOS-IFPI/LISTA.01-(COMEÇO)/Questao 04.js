4. // Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).

import { question } from "readline-sync"

console.log ('...Conversor de dolar para real...')

// Entrada 

var valor_em_dolar = Number(question('Quantidade de dolares: '))

var valor_do_dolar = Number(question("Cotação do dolar atualmente: "))

// Processamento

const valor_em_real = valor_do_dolar * valor_em_dolar

// Saida

console.log (`o valor em real depois da conversão é: ${valor_em_real} reais `)


