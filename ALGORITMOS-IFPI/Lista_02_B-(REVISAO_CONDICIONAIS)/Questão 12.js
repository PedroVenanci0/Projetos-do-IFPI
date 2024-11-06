/**12. Leia um número e escreva se o número é inteiro ou decimal. */

import { get_number } from "../Exportar/io_utils.js";

console.log ("#### Inteiro ou Descimal ####")

function main(){

    // Entrada 

    const numero = get_number("Informe o numero: ")

    // Processamento 

    const inteiro_ou_descimal = identificando_inteiro_ou_descimal(numero)

    // Saida 

    console.log (inteiro_ou_descimal)
}

function identificando_inteiro_ou_descimal(numero){

    const subtraindo_inteiro = numero - Math.trunc(numero) 

    if (subtraindo_inteiro === 0){

        return "O número é INTEIRO"

    }else {

        return "O número é DESCIMAL"
    }
}

main()