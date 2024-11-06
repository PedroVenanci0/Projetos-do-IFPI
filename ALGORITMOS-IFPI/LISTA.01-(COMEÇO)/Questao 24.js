// 24. Leia um valor em m, calcule e escreva o equivalente em cm.

import { question } from "readline-sync"

console.log ('conversor de metros para centimetros')

// Entrada 

var metro = Number(question('Informe o valor em metros: '))

// processamento

const centimetros = metro * 100

// Saida 

console.log (` ${metro} metros equivalem a ${centimetros} centimetros `)