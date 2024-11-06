// 41. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). 
// Supondo que a porcentagem do distribuidor seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

import { question } from "readline-sync"

console.log ('Quanto custa um carro novo?')

// Entrada

var custo_de_fabrica = Number(question("informe o custo de fabrica de um carro novo: "))

// Processamento 

const distribuidor = (custo_de_fabrica * 28/100)

const impostos = (custo_de_fabrica * 45/100)

const custo_ao_consumidor = custo_de_fabrica + distribuidor + impostos

// Saida 

console.log (`O custo ao consumidor é de ${custo_ao_consumidor} reais`)