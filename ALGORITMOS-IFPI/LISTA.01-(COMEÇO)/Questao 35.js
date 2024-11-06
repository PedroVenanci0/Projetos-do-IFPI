// 35. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.: número = 9534 ; soma = 9+5+3+4 = 21.

import { question } from "readline-sync"

console.log ('somatorio dos elementos de um numero')

// Entrada

var numero = Number(question('Informe um numero inteiro de 4 dígitos: '))

// Processamento

const unidade_milhar = Math.trunc(numero / 1000)

const centena = (Math.trunc (numero / 100)) % 10 

const dezena = Math.trunc((numero % 100) / 10)

const unidade = ((numero % 100) % 10)

const soma = unidade_milhar + centena + dezena + unidade

// Saida 

console.log (`O somatorio dos elementos do número informado é ${soma}`)