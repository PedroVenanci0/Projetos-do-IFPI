// 36. Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

import { question } from "readline-sync"

console.log ('calculadora de idade expressa em dias')

// Entrada 

var anos = Number(question("Informe sua idade exata em anos: "))

var meses = Number(question("Informe o restante da sua idade extamente em meses: "))

var dias = Number(question('informe o que sobrou em dias: '))

// Processamento

const dias_totais = (anos * 365) + (meses * 30) + dias

// Saida 

console.log (`Sua idade corresponde a ${dias_totais} dias`)