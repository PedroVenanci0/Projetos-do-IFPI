// 21. Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for maior do que ou igual a 0,5, 
// o numero é arredondado para o inteiro imediatamente superior, caso contrario, é arredondado para o inteiro imediatamente inferior.

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Arredondando Números #### ")

function main(){

    // Entrada

    const numero_nao_inteiro = get_number("Informe um número não inteiro (ex: 30.5): ")

    // Processamento

    const numero_arredondado = arredondado(numero_nao_inteiro)

    // Saida

    console.log (`O resultado no arredondamento do número ${numero_nao_inteiro} é ${numero_arredondado}`)


}

function arredondado(numero_nao_inteiro){

    if (numero_nao_inteiro % 1 >= 0.5){

        return (Math.ceil(numero_nao_inteiro))
}
    else {

        return (Math.trunc(numero_nao_inteiro))
}


}

main()