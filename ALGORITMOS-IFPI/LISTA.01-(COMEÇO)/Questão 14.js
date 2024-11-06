// 14. Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.

import { question } from "readline-sync"

console.log ('calculador de média ponderada')

// Entrada

var nota_1 = Number(question('Qual a primeira nota do aluno: '))

var peso_1 = Number(question('Qual o peso da primeira nota: '))

var nota_2 = Number(question('Qual a segunda nota do aluno: '))

var peso_2 = Number(question('Qual o peso da segunda nota: '))

var nota_3 = Number(question('Qual a terceira nota do aluno: '))

var peso_3 = Number(question('Qual o peso da terceira nota: '))

// Processamento

const media = ([(nota_1*peso_1) + (nota_2*peso_2) + (nota_3*peso_3)] / (peso_1 + peso_2 + peso_3)).toFixed(2)

// Saida 

console.log (
    
    `a média ponderada do aluno foi de ${media} pontos`
    
    )

