/**9. Leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda etc.), se digitar outro
valor deve aparecer valor inválido. */

import { get_number } from "../Exportar/io_utils.js";

console.log ("#### DIA CORREPONDETE AO NÚMERO #### ")

function main(){

    // Entrada

    console.log ("Dígite 1 para Domingo, 2 para Segunda, 3 para terça e assim sucessivamente ate o 7 correpsonder ao Sabado")

    const numero = get_number("Informe o dígito correspondente ao dia: ")

    // processamento 

    const qual_o_dia = identificando_dia(numero)

    // Saida

    console.log (qual_o_dia)




}
function identificando_dia(numero){

    if (numero === 1){

        return "1 - Domingo"
    }
    else if (numero === 2){

        return "2 - Segunda"
    }
    else if (numero === 3){

        return "3 - Terça"
    }
    else if (numero === 4){

        return "4 - Quarta"
    }
    else if (numero === 5){

        return "5 - Quinta"
    }
    else if (numero === 6){

        return "6 - Sexta"
    }
    else if (numero === 7){

        return "7 - Sabado"
    }
    else {

        return "Valor INVÁLIDO"
    }
}
main()