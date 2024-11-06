// 39. Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão: D = (R + S) / 2 ; onde R = (A + B)**2 ; S = (B + C)**2

import { question } from "readline-sync"

console.log ('expressão númerica')

// Entrada 

var numero_A = Number(question("Informe o primeiro numero inteiro: "))

var numero_B = Number(question("Informe o segundo numero inteiro: "))

var numero_C = Number(question("Informe o terceiro numero inteiro: "))

// Processamento 

const incognita_R = (numero_A + numero_B)**2

const incognita_S = (numero_B + numero_C)**2

const expressão_D = ((incognita_R + incognita_S) / 2).toFixed(2)

// Saida 

console.log (`O resultado da expressao é ${expressão_D}`)