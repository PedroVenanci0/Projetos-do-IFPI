// 22. Leia um valor em km, calcule e escreva o equivalente em m.

import { question } from "readline-sync"

console.log ('conversor de medidas km (quilometros) para m (metros)')

// Entrada 

var km = Number(question('Informe a quantidade de quilometros: '))

// Processamento 

const m = km * 1000 

// Saida 

console.log (`O valor em metros é de ${m}`)
