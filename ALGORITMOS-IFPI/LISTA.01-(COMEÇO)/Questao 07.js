// 7. Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.

import { question } from "readline-sync";

console.log ("soma e diferença entre os termos")

// Entrada

var primeiro = Number(question("Digite o primeiro número>: "))

var segundo = Number(question('Digite o segundo número: '))

var terceiro = Number(question("Digite o terceiro número: "))

// Processamento

var soma = (primeiro) + (segundo)

var diferença = (segundo) - (terceiro)

// saida 

console.log (`a soma dos dois primeiro númeoros digitados é ${soma}, já a diferença entre os dois ultimos é ${diferença}`)