// 26. Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

import { question } from "readline-sync"

console.log ('contador de dias e semanas')

// Entrada 

var dias = Number(question('Informe o número inteiro de dias: '))

// Processamento

const semanas = Math.trunc(dias / 7)
const dias_sobra = Math.floor(dias % 7)

// Saida 

console.log (`o numero convertido corresponde a ${semanas} semanas e ${dias_sobra} dias`)