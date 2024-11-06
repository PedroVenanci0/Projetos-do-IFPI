// 34. Leia 3 números, calcule e escreva a média dos números.

import { question } from "readline-sync"

console.log ('Calculando a media')

// Entrada

var primeiro_numero = Number(question('Informe o primeiro numero inteiro: '))

var segundo_número = Number(question('Informe o segundo número inteiro: '))

var terceiro_numero = Number(question("Informe o terceiro número inteiro: "))

// Processamento 

const media = (primeiro_numero + segundo_número + terceiro_numero) / 3

// Saida 

console.log (`A média dos npumeros corresponde a ${media}`)

