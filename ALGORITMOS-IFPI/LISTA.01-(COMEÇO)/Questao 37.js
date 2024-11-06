// 37. Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

import { question } from "readline-sync"

console.log ('calculando sua idade de dias para anos, meses e dias')

// Entrada 

var dias = Number(question('Informe sua idade em dias: '))

// Processamento

const anos = Math.trunc(dias / 365)

const meses =  Math.trunc((dias % 365) / 30)

const dias_sobras = Math.trunc((dias % 365) % 30)

// Saida 

console.log (`Sua idade corresponde a ${anos} anos, ${meses} meses e ${dias_sobras} dias`)