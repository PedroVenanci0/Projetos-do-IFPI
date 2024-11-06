// 3. Leia 3 (três) números, verifique e escreva o maior entre os números lidos.

import { get_number, print } from "../Exportar/io_utils.js";

function main(){

const numero_01 = get_number("Informe o primeiro número: ")
const numero_02 = get_number("Informe o segundo número: ")
const numero_03 = get_number("Informe o terceiro número: ")

print (`${maior_numero(numero_01,numero_02,numero_03)}`)


}

function maior_numero(numero_01, numero_02 , numero_03){

    if ((numero_01 > numero_02) && numero_01 > numero_03)

    return (`O número ${numero_01} é o maior entre os lidos`)

    else if ( (numero_02 > numero_01) && numero_02 > numero_03)

    return (`O número ${numero_02} é o maior entre os lidos`)

    else if ((numero_03 > numero_02) && numero_03 > numero_01)

    return (`O número ${numero_03} é o maior entre os lidos`)



}

main ()