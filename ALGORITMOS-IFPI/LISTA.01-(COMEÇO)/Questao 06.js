// 6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)

import { question } from "readline-sync";

console.log ('conversor de km/h para m/s')

// Entrada 

var kilometro  = Number(question('Informe a velocidade em km/h: '))

// Processamento

var metros_por_segundo = (kilometro / 3.6).toFixed(2)

//saida 

console.log (`O valor da conversao de Km/h para m/s é: ${metros_por_segundo} m/s`)

