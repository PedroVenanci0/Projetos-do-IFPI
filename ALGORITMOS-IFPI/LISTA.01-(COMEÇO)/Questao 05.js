// 5. Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).

import { question } from "readline-sync";

console.log ('somatorio dos elementos de um numero inteiro')

// Entrada 

var Numero = Number(question("Informe o numero inteiro a ser usado: "))

// Processamento

const centena = Math.trunc(Numero / 100)

const resto = (Numero % 100)

const dezena = Math.trunc(resto / 10)

const unidade = resto % 10

const somatorio = centena + dezena + unidade

// Saida

console.log (` o resultado do somatorio dos elementos do numero foi: ${somatorio}`)