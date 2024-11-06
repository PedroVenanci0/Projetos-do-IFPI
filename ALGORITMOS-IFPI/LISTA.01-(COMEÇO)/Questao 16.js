// 16. Leia o valor do lado de um quadrado, calcule e escreva sua área. (área = lado2)

import { question } from "readline-sync";

console.log ('Área do quadrado')

// Entrada

var lado = Number(question('Informe o lado do quadrado: '))

// processamento

const area = lado ** 2

// Saida 

console.log (`A área do quadrado corresponde a ${area} metros quadrados `)
