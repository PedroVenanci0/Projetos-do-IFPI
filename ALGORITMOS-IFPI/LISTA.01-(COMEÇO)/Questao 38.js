// 38. Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.

import { question } from "readline-sync"

console.log ('soma de duas fracoes')

// Entrada 

var numerador_fraçao_1 = Number(question('Informe o numerador da primeira fracao:  '))

var denominador_fraçao_1 = Number(question("Informe o denominador da primeira fracao: "))

var numerador_fraçao_2 = Number(question("Informe o numerador da segunda fracao: "))

var denominador_fraçao_2 = Number(question("Informe o denominador da segnda fracao: "))

// Processamento

// mmc (minimo multiplicador comum)

const mmc = denominador_fraçao_1 * denominador_fraçao_2

const resultado_da_soma = (((mmc / denominador_fraçao_1) * numerador_fraçao_1) + ((mmc / denominador_fraçao_2) * numerador_fraçao_2)) 

// Saida

console.log (`O resultado da soma entre as duas frações foi ${resultado_da_soma}/${mmc}`)