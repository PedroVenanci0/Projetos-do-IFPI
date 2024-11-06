// 31. Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

import { question } from "readline-sync"

console.log ('conversor de numeors binarios')

// Entrada 

var numero = Number(question("Informe um numero inteiro de 4 dígitos binários : "))

// Processamento

const primeiro_binario = ((numero % 10) *  2**0 )

const segundo_binario = (Math.trunc((numero % 10) / 10)) * 2**1

const terceiro_binario = (Math.trunc((numero % 100) / 10)) * 2**2

const quarto_binario = (Math.trunc(numero / 1000)) * 2**3



const decimal = primeiro_binario + segundo_binario + terceiro_binario + quarto_binario


// Saida

console.log (`A base decimal equivale a ${decimal}`)
