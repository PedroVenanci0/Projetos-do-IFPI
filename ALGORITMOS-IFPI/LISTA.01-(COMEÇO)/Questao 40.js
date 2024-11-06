//  Calcule a quantidade de dinheiro gasta por um fumante. 
// Dados de entrada: o número de anos que ele fuma, o no de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

import { question } from "readline-sync"

console.log ('Total de dinheiro gasto com cigarros')

// Entrada

var anos_fumando = Number(question("Informe o numero de anos que fuma: "))

var cigarro_dia = Number(question("Informe o numero de cigarros por dia: "))

var carteira_preço = Number(question("Informe o preco da carteira de cigarros: "))

// Processamento 

const dias_fumando = anos_fumando * 365 

const total_de_cigarros_consumidos = (dias_fumando * cigarro_dia)

const total_de_dinheiro_gasto = (total_de_cigarros_consumidos / 20) * carteira_preço

// Saida 

console.log (`O total de dinheiro gasto com carteiras de cigarro foi de ${total_de_dinheiro_gasto} reais`)