// 5. Leia 3 (três) números e escreva-os em ordem crescente.


import { get_positivo_number, print } from "../Exportar/io_utils.js";

function main(){

    const numero_01 = get_positivo_number("numero 01: ")
    const numero_02 = get_positivo_number("numero 02: ")
    const numero_03 = get_positivo_number("numero 03: ")

    
    print (`${ordem_crescente(numero_01, numero_02, numero_03)}`)

    
}

function ordem_crescente(numero_01, numero_02, numero_03){

    if (numero_01 >= numero_02 && numero_03 <= numero_02)
        
        return (`A ordem crescente dos números digitados é ${numero_03}, ${numero_02}, ${numero_01}`)

        else if (numero_01 >= numero_03 && numero_02 <= numero_03)

        return (`A ordem crescente dos números digitados é ${numero_02}, ${numero_03}, ${numero_01}`)

        else if (numero_02 >= numero_01 && numero_03 <= numero_01)

        return (`A ordem crescente dos números digitados é ${numero_03}, ${numero_01}, ${numero_02}`) 

        else if (numero_02 >= numero_03 && numero_01 <= numero_03)

        return (`A ordem crescente dos números digitados é ${numero_01}, ${numero_03}, ${numero_02}`)

        else if (numero_03 >= numero_01 && numero_01 <= numero_02)

        return (`A ordem crescente dos números digitados é ${numero_01}, ${numero_02}, ${numero_03}`)

        else if (numero_03 >= numero_02 && numero_02 <= numero_01)

        return (`A ordem crescente dos números digitados é ${numero_02}, ${numero_01}, ${numero_03}`)


   

}




main()