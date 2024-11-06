// 33. Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso. (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).

import { question } from "readline-sync"

console.log ('calculando o somatorio entra um número e seu inverso')

// Entrada 

var numero = Number(question('Informe um número inteiro de 3 dígitos: '))

// Processamento 

const centena = Math.trunc(numero / 100)

const dezena = Math.trunc((numero % 100) / 10)

const unidade = numero % 10

const somatorio = numero + ((unidade * 100) + (dezena * 10) + (centena))

3
4
5

// Saida 

console.log (`O somatorio entre o número inserido e seu inverso é de ${somatorio} `)