// 15. Leia o valor da base e altura de um triângulo, calcule e escreva sua área. (área=(base * altura)/2)

import { question } from "readline-sync"

console.log ('Área do triângulo')

// Entrada 


var base = Number(question('Informe a base do triangulo: '))

var altura = Number(question('Informe a altura do triangulo: '))

// processamento 

const area = (base * altura) / 2

// Saida 

console.log (`A área do triangulo corresponde a ${area} metros quadrados`)
