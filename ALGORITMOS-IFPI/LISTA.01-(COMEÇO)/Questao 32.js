// 32. Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.

import { question } from "readline-sync"

console.log ('calculando a diferença entra um número e seu inverso')

// Entrada 

var numero = Number(question('Informe um número inteiro de 3 dígitos: '))

// Processamento 

const centena = Math.trunc(numero / 100)

const dezena = Math.trunc((numero % 100) / 10)

const unidade = numero % 10

const diferença = numero - ((unidade * 100) + (dezena * 10) + (centena))

// Saida 

console.log (`A diferença entre o número inserido e seu inverso é de ${diferença} `)

