// 15. Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
// Escreva na tela qual dos professores tem salário total maior.

import { question } from "readline-sync";

console.log ("#### Qual dos salários é o maior ####")

function main(){

    // Entrada

    const horas_aula_prof_01 = Number(question("Informe a quantidade de horas aula foram dadas pelo primeiro professor: "))
    const valor_aula_prof_01 = Number(question("Agora informe o valor por hora aula do primeiro professor: "))

    const horas_aula_prof_02 = Number(question("Informe a quantidade de horas aula foram dadas pelo segundo professor: "))
    const valor_aula_prof_02 = Number(question("Agora informe o valor por hora aula do segundo professor: "))

    // processamento

    const salario = maior_salario(horas_aula_prof_01, valor_aula_prof_01, horas_aula_prof_02, valor_aula_prof_02)

    // saida

    console.log (salario)

}

function maior_salario(horas_aula_prof_01, valor_aula_prof_01, horas_aula_prof_02, valor_aula_prof_02){

const salario_prof_01 = horas_aula_prof_01 * valor_aula_prof_01
const salario_prof_02 = horas_aula_prof_02 * valor_aula_prof_02

if (salario_prof_01 > salario_prof_02)

return (`O Salários do primeiro professor é maior do que do segundo `)

else if (salario_prof_01 < salario_prof_02)

return (`O Salários do segundo professor é maior do que do primeiro `)

else if (salario_prof_01 === salario_prof_02)

return ("O salário dos dois professores são iguais")
}

main()