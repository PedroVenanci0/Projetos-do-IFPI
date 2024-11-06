// Leia a data atual (dia , mês, ano) e data de nascimento(dia, mês e ano) de uma pessoa, 
// calcule e escreva sua idade exata (em anos)

import {question} from "readline-sync"

function main(){

    const dia_nascimento = Number(question("Informe o dia do seu nascimento: "))
    const mes_nascimento = Number(question('Informe seu mês de nascimento: '))
    const ano_nascimento = Number(question("Informe seu ano de nascimento: "))

    const dia_atual = Number(question("Informe o dia atual: "))
    const mes_atual=  Number(question("Informe o mês atual: "))
    const ano_atual = Number(question("Informe o ano atual: "))


    console.log (calcular_idade(mes_atual, mes_nascimento, dia_atual, dia_nascimento, ano_atual, ano_nascimento))


}

function calcular_idade(mes_atual, mes_nascimento, dia_atual, dia_nascimento, ano_atual, ano_nascimento){

    if (mes_atual < mes_nascimento){

      return (ano_atual - ano_nascimento)- 1
    }

    else if ( mes_atual === mes_nascimento && dia_nascimento > dia_atual){ 


        return (ano_atual - ano_nascimento)- 1
    }

    else {

        return (ano_atual - ano_nascimento)
    }

    



}

    




main()
