// Uma loja vende seus produtos no sistema entrada mais duas prestações, sendo a entrada maior ou igual a
// cada uma das duas prestações; estas devem ser iguais, inteiras e as maiores possíveis. Por exemplo, se o
// valor da mercadoria for R$ 270,00, a entrada e as duas prestações são iguais a R$ 90,00; se o valor da
// mercadoria for R$ 302,00, a entrada é de R$ 102,00 e as duas prestações são iguais a R$ 100,00.
// Escreva um algoritmo que receba o valor da mercadoria e forneça o valor da entrada e das duas prestações, de acordo com as regras acima.

import { question } from "readline-sync"

console.log ('calculando o valor da entrada e suas prestaçoes')

// Entrada 

var mercadoria = Number(question('Informe o valor da mercadoria:  '))

// Processamento 

const resto = Math.trunc (mercadoria % 3)

const entrada = Math.trunc (mercadoria / 3) + resto

const prestaçoes = Math.trunc (mercadoria / 3)

// Saida 

console.log (`o valor da entrada corresponde a ${entrada} reais e os valores das duas prestaçoes sao de ${prestaçoes} reais`)

