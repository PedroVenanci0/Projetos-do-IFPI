 // 44. Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a
 // quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada pelo usuário.

 import { question } from "readline-sync"

 console.log ('calculando a quantidade dos componetes presentes em um latao')

 // Entrada 

 var peso_latao = Number(question('Informe o peso em quilogramas do latao:  '))

 // processamento 

 const cobre = (peso_latao * 70/100)

 const zinco = (peso_latao * 30/100)

 // Saida 

 console.log (`A quantidade de cobre existente no latao é de ${cobre} kg (quilogramas)`)

 console.log (`A quantidade de zinco existente no latao é de ${zinco} kg (quilogramas)`)

