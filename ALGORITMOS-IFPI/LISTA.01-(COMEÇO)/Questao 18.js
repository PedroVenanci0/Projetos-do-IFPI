// 18. Leia o valor do raio de uma circunferência, calcule e escreva seu comprimento.(c = 2 * p * r)

import { question } from "readline-sync"

console.log ('calculador de comprimento')

// Entrada 

var raio = Number(question('Informe o numero correspondente ao raio da circunferência: '))

// Processamento 

const comprimento = (2 * 3.14 * raio).toFixed(2)

// Saida 

console.log (`O comprimento da circunferênca corresponde a ${comprimento}`)