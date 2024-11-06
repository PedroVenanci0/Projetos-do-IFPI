// 23. Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Qual data é a mais recente #### ")

function main(){

    // Entrada

    console.log ("Escreva duas datas onde, o dia menor que 31 e o mes menor que 12")

    const dia_data_01 = get_number("Informe o dia da primeira data: ") 
    const mes_data_01 = get_number("Informe o mês da primeira data: ") 
    const ano_data_01 = get_number("Informe o ano da primeira data: ") 
    const dia_data_02 = get_number("Informe o dia da segunda data: ") 
    const mes_data_02 = get_number("Informe o mês da segunda data: ") 
    const ano_data_02 = get_number("Informe o ano da segunda data: ")
    
    // Processamento 

    const data_recente = localizando_data(dia_data_01, mes_data_01, ano_data_01, dia_data_02, mes_data_02, ano_data_02)

    // Saida 

    console.log (data_recente)

}

function localizando_data( d_01, m_01, a_01, d_02, m_02, a_02){

    if (d_01 > 31 || d_02 > 31){

        return "Valor invalido"
    }
    else if (m_01 > 12 || m_02 > 12){

        return "valor inválido"
    }

    if  (a_01 > a_02){

        return "A primeira data é a mais recente"
    }
    else if ( a_01 === a_02 && m_01 > m_02){

        return "A primeira data é a mais recente"
    }
    else if (a_01 === a_02 && m_01 === m_02 && d_01 > d_02){

        return "A primeira data é a mais recente"
    }
    else  if (a_02 > a_01){

        return "A segunda data é a mais recente"
    }
    else if ( a_02 === a_01 && m_02 > m_01){

        return "A segunda data é a mais recente"
    }
    else if ( a_02 === a_01 && m_02 === m_01 && d_02 > d_01){

        return "A segunda data é a mais recente"
    }
    else if ( a_02 === a_01 && m_02 === m_01 && d_02 === d_01){

        return "As datas são iguais"
    }


    


}

main()