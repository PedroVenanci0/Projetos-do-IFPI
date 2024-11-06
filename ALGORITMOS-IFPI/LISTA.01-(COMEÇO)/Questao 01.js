// Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)

import {question} from "readline-sync"

// Entrada

const velocidade_ms = Number(question('Qual a velocidade em m/s: '))

// processamento 

const velocidade_km = velocidade_ms * 3.6

//saida

console.log  (`O resultado da conversão de velocidade é ${velocidade_km} km/h (quilometros por hora)`) 


    