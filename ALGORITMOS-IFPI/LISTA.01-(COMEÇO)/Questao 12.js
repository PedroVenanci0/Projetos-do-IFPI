// 12. Leia o salário de um trabalhador e escreva seu novo salário com um aumento de 25%.

import { question } from "readline-sync";

console.log ('calculador de aumento por porcentagem')

// Entrada 

var salário_sem_aumento = Number(question('Informe seu salário antes do aumento: '))

// Processamento 

const salário_com_aumento = (salário_sem_aumento * 25/100) + salário_sem_aumento

// Saida 

console.log (`Seu salário atual com aumento correponde à: ${salário_com_aumento} reais `)