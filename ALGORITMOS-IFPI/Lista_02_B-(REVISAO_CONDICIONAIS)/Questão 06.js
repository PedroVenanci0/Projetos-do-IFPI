/**6. Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino ou N para Noturno e
escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. */

import { question } from "readline-sync";
import { get_number } from "../Exportar/io_utils.js";

console.log (" **** Qual o seu turno **** ")

function main(){

    // Entrada 

    console.log ("Dígite M para matutino, V para Vespertino e N para noturno ")

    const turno = question("Informe seu turno: ")

    // processamento 

    const Qual_o_turno = identificando_turno(turno).toUpperCase



    // Saida 

    console.log (Qual_o_turno)

}

function identificando_turno(turno){

    if (turno === "M"){

        return "Bom dia!"
    }
    else if (turno === "V"){

        return "Bom Tarde!"
    }
    else if (turno === "N"){

        return "Bom noite!"
    }

    else {

        return "Valor inválido"
    }


}

main()