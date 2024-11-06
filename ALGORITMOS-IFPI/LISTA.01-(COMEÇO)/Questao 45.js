// Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para 
// decidir o numero de notas de cada valor que deve ser disponibilizado para o cliente que realizou o saque.
// Um possível critério seria o da "distribuição ótima" no sentido de que as notas de menor valor
// disponíveis fossem distribuídas em número mínimo possível. Por exemplo, se a maquina só dispõe de
// notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo deveria
// indicar uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um
// algoritmo que receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com o
// critério da distribuição ótima.

import { question } from "readline-sync"

console.log (" caixa eletronico (somente saque) ")

// Entrada 

var saque = Number(question("Informe o valor do saque: "))

// processamento 

const nota_50 = Math.trunc (saque / 50)

const nota_10 = Math.trunc ((saque % 50) / 10)

const nota_5 = Math.trunc (((saque % 50) % 10) / 5)

const nota_1 = Math.trunc ((((saque % 50) % 10) % 5) / 1)

// Saida 

console.log (`A distribuiçao ideal do valor a ser sacado é ${nota_50} nota(s) de R$ 50, ${nota_10} nota(s) de R$ 10, ${nota_5} nota(s) de R$ 5 e ${nota_1} nota(s) de R$ 1`)

console.log (`Totabilizando o valor a ser requerido no saque, que é ${saque} reais`)
