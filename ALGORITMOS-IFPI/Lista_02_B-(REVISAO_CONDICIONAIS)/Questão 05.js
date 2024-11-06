/**5. Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é
sempre pelo mais barato. */

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### INFORMANDO O MELHOR PREÇO #### ")

function main(){

    // Entrada 

    const prod_01 = get_number("Informe o valor do primeiro produto: ")
    const prod_02 = get_number("Informe o valor do segundo produto: ")
    const prod_03 = get_number("Informe o valor do terceiro produto: ")

    // processamento

    const Qual_o_mais_barato =  mais_barato(prod_01, prod_02, prod_03)

    // Saida 

    console.log (`O produto mais barato corresponde ao produto com valor de ${Qual_o_mais_barato} reias`)


}

function mais_barato(prod_01, prod_02, prod_03){

    if (prod_01 < prod_02 && prod_01 < prod_03){

        return prod_01
    }
    else if (prod_02 < prod_01 && prod_02 < prod_03){

        return prod_02
    }

    else if (prod_03 < prod_01 && prod_03 < prod_02){

        return prod_03
    }

}
main()