// 30. Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde.

import { question } from "readline-sync"

console.log ('conversor de minutos para dias e sua sobras')

// Entrada 

var minutos = Number(question('Informe o número inteiro em minutos: '))

// Processamento 


const dias = Math.trunc ((minutos / 60) / 24)

const horas =  Math.trunc((minutos / 60) % 24)

const minutos_sobras = ((minutos % 60)  % 24)

// Saida 

console.log (`O número inserido em minutos corresponde a ${dias} dias, ${horas} horas e ${minutos_sobras} minutos   `)

