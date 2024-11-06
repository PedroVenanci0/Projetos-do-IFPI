// 19. Leia o valor do raio de uma esfera, calcule e escreva seu volume.(v = (4 * p * r3) / 3) (p = 3,14)

import { question } from "readline-sync"

console.log ('calculador do volume de uma esfera')

// Entrada 

var raio = Number(question('Informe o valor do raio da esfera: '))

// Processamento 

const volume = ((4 * 3,14 * raio**3) / 3).toFixed(2)

// Saida 

console.log (`O volume da esfera corresponde a ${volume} m^3(metros cubicos) `)