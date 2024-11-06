// 27. Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

import { question } from "readline-sync"

console.log ('mensuração de tempo')

// Entrada

var segundos = Number(question('Informe um número inteiro em segundos: '))

// processamento

const horas = Math.trunc((segundos / 60) / 60)

const minutos = Math.floor((segundos / 60) % 60)

const segundos_sobra = (segundos % 60)



// Saida

console.log (`o valor mensurado corresponde a ${horas} horas, ${minutos} minutos e ${segundos_sobra} segundos`)
