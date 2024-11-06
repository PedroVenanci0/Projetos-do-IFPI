// 1. Leia um número e mostre na tela se o número é positivo ou negativo.

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Positivo ou Negativo #### ")

function main(){

    // Entrada 

    const numero = get_number("Informe um numero: ")

    // Processamento 

    const positivo_ou_negativo = classificando_numero(numero) 


    // Saida 

    console.log (positivo_ou_negativo)


}

function classificando_numero(numero){

    if (numero >= 0){

        return `O número ${numero} é POSITIVO`

    } else {

        return `O número ${numero} é NEGATIVO`

    } 


    
}

main()