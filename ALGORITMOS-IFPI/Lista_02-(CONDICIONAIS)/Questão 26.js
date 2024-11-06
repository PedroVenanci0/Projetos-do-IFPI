// 26. Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### identificando hipotenusa e seus catetus ")

function main(){

    // Entrada 

    const lado_01 = get_number("Informe o primeiro lado do triângulo: ")
    const lado_02 = get_number("Informe o segundo lado do triângulo: ")
    const lado_03 = get_number("Informe o terceiro lado do triângulo: ")

    // Processamento

    const hipotenusa = identificando_hipotenusa(lado_01, lado_02, lado_03)


    // Saida

    console.log (`${hipotenusa} `)

}
function identificando_hipotenusa(L_01, L_02, L_03){

    if (L_01 > L_02 && L_01 > L_03){

        return (`A hipotenusa correponde a ${L_01} e os cateteus correpondem a ${L_02} e ${L_03} `)
    }
    else if (L_02 > L_01 && L_02 > L_03){      

        return (`A hipotenusa correponde a ${L_02} e os cateteus  correpondem a ${L_01} e ${L_03} `)
    }
    else if (L_03 > L_01 && L_03 > L_02){

        return (`A hipotenusa correponde a ${L_03} e os cateteus  correpondem a ${L_01} e ${L_02} `)
    }

    else {

        return "Não é um triângulo retângulo, logo não há hipotenusa"
    

}
}
main()