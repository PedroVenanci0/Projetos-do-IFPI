// 17. Leia o valor da base e altura de um retângulo, calcule e escreva sua área. (área = base * altura)

import { question } from "readline-sync"

console.log ('Área do retângulo')

// Entrada

var base = Number(question('Informe o número correspondente a base do retângulo: '))

var altura = Number(question('Informe o número corespondente a altura do retângulo: '))

// processamento 

const area = base * altura

// Saida 

console.log (`A área do retângulo é correspondente a: ${area} metros quadrados`)