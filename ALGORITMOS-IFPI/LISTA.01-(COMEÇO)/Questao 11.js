// 11. Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)

import { question } from "readline-sync"

console.log ('ordem inversa dos números')

// Entrada

var numero = Number(question('Digite o número inteiro a ser usado: '))

// Processamento

const centena = Math.trunc(numero / 100)

const Dezena = Math.trunc((numero % 100) / 10)

const unidade = (numero % 10)

// Saida

console.log (`A ordem inversa do número apresentado anteriormente é ${unidade}${Dezena}${centena}`)
