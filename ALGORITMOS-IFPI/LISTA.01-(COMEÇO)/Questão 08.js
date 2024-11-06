// 8. Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

import { question } from "readline-sync";

console.log ('Divisão da soma pela diferença')

// Entrada 

var primeiro = Number(question("Digite o primeiro número a ser usado: "))

var segundo = Number(question("Digite o segundo número a ser usado: "))

// Processamento 

var soma = primeiro + segundo

var diferença = primeiro - segundo

var divisao = soma / diferença 

// Saida 

console.log (`a divisão da soma pela subtração dos termos corresponde à: ${divisao}`)