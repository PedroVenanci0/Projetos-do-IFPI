// 10. Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.

import { question } from "readline-sync"


console.log ("#### Validando Data ####" )

function main(){

    // Entrada 

    const dia = Number(question("Informe o dia: "))
    const mês = Number(question("Informe o mês: "))
    const ano = Number(question("Informe o ano: "))

    // processamento

    const data_valida = validando_data(dia, mês, ano)

    // saida 

    console.log (data_valida)
    
}

function validando_data(D,M,A){

    if  ( D > 31 || M > 12 || A <= 0 || D === 0 || M === 0 ){

    return "Data inválida"

    }

    else {

        return "Data válida"
    }


}


main()