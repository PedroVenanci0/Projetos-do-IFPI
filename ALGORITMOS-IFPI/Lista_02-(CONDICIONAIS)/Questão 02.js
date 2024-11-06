// 2. Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.

import { get_number, print } from "../Exportar/io_utils.js";

function main(){

    const numero_01 = get_number("Informe o primeiro número: ")
    const numero_02 = get_number("Informe o segundo número:  ")



print (`${maior_e_menor_entre(numero_01, numero_02)}`)

}

function maior_e_menor_entre( numero_01, numero_02){

if ( numero_01 > numero_02)

return (`O número ${numero_01} é o maior e o número ${numero_02} é o menor `)

else if ( numero_01 < numero_02)

return (`O número ${numero_02} é o maior e o número ${numero_01} é o menor`)

else if ( numero_01 === numero_02)

return (`Os dois números são iguais`)

}



main()