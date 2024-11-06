// 13. Leia um valor em real (R$), calcule e escreva 70% deste valor.

import { question } from "readline-sync";

console.log ('calculador de aumento por porcentagem ')

// Entrada 

var Real = Number(question('Informe o número de reais que receberão o aumento: '))

// Processamento 

var aumento = Real * 70/100

// Saida 

console.log (`O valor correspondente a 70% do anterior é: ${aumento} reais`)