// 29. Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

import { question } from "readline-sync"

console.log ('converosr de meses para anos')

// Entrada 

var meses = Number(question('Informe o número inteiro de meses: '))

// Processamento 

const anos = Math.trunc(meses / 12)
const meses_sobra = Math.trunc(meses % 12) 

// Saida 

console.log (`o número de meses foi convertido para ${anos} anos e ${meses_sobra} meses `)

