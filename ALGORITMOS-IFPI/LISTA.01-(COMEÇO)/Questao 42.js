// 42. Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles, conforme fórmula abaixo.
// D = math.sqrt (x2 - x1)**2 + (y2 - y1)**2   

import { question } from "readline-sync"

console.log ('Distancia entre pontos')

// Entrada 

var ponto_1_x1 = Number(question("Informe o valor do ponto_1 que toca o eixo x:  "))

var ponto_1_y1 = Number(question('Informe o valor do ponto_1 que toca o eixo y: '))

var ponto_2_x2 = Number(question('Informe o valor do ponto_2 que toca o eixo x: '))

var ponto_2_y2 = Number(question('Informe o valor do ponto_2 que toca o eixo y: '))

// Processamento 

const distancia = (Math.sqrt((ponto_2_x2 - ponto_1_x1)**2 + (ponto_2_y2 - ponto_1_y1)**2)).toFixed(2)

// Saida 

console.log (`A distancia entre os dois pontos indicados é ${distancia}`)