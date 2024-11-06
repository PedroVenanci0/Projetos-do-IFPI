// 43. Um sistema de equações lineares do tipo, pode ser resolvido segundo mostrado abaixo

// x = ((c * e) - (b * f)) / ((a * e) - (b * d))

// y = ((a * f) - (c * d)) / ((a * e) - (b * d))

// Escreva um algoritmo que leia os coeficientes a, b, c, d, e e f, calcule e escreva os valores de x e y.

import { question } from "readline-sync"

console.log ('calculando valor de x e y')

// Entrada 

var coeficiente_A =  Number(question('Informe o valor do coeficiente a: '))

var coeficiente_B =  Number(question('Informe o valor do coeficiente b: '))

var coeficiente_C =  Number(question('Informe o valor do coeficiente c: '))

var coeficiente_D =  Number(question('Informe o valor do coeficiente d: '))

var coeficiente_E =  Number(question('Informe o valor do coeficiente e: '))

var coeficiente_F =  Number(question('Informe o valor do coeficiente f: '))

// Processamento 

const valor_X = ((coeficiente_C * coeficiente_E) - (coeficiente_B * coeficiente_F)) / ((coeficiente_A * coeficiente_E) - (coeficiente_B * coeficiente_D))

const valor_Y = ((coeficiente_A * coeficiente_F) - (coeficiente_C * coeficiente_D)) / ((coeficiente_A * coeficiente_E) - (coeficiente_B * coeficiente_D))

// Saida 

console.log (`o valor de X é igual a ${valor_X}; ja o valor de Y corresponde a ${valor_Y}`)
