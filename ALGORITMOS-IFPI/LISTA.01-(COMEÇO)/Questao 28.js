// 28. Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.

import { question } from "readline-sync"

console.log ('conversor de dias para semanas')

// Entrada

var horas = Number(question('Informe o número inteiro de horas: '))

// Processamento 


const semanas = Math.trunc(Math.trunc( horas / 24) / 7) 

const dias = Math.trunc((horas / 24) % 7)

const horas_sobra = Math.trunc(horas % 24)



// Saida 

console.log (`o número de horas foi convertido em ${semanas} semanas, ${dias} dias e ${horas_sobra} horas`)
