// 25. Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.

import { question } from "readline-sync"

console.log ('conversor de medidas')

// Entrada

var metro = Number(question('Informe o número inteiro em metros: '))

// processamento 

const kilometro = Math.trunc(metro / 1000)
const metros_sobra = (metro % 1000)

// Saida

console.log (`O resultado da concersão corresponde a ${kilometro} kilometros e ${metros_sobra} metros`)
