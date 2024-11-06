// 10. Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1o pelo 2o.

import { question } from "readline-sync";

console.log ('Quociente e resto de dois números inteiros')

// Entrada

var primeiro = Number(question('Digite o primeiro número inteiro: '))

var segundo = Number(question("Digite o segundo número inteiro: "))

// processamento

var quociente = Math.trunc(primeiro / segundo)

var resto = (primeiro % segundo)

// Saida 

console.log (`O quociente da divisão dos números foi ${quociente}, já o resto foi ${resto}`)