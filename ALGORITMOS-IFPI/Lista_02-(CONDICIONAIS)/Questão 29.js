// 29. Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas formadas pelos seus dois primeiros e dois últimos dígitos.
// Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
// Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Quadrado perfeito #### ")

function main(){

    // Entrada 

    const numero = get_number("Informe um número de 4 dígitos: ")

    // Processamento

    const quadrado_perfeito = validando_quadrado_perfeito(numero)

    // Saida

    console.log (quadrado_perfeito)

}
function validando_quadrado_perfeito(numero){

    const dezena_01 = Math.trunc(numero / 100)
    const dezena_02 = Math.trunc(numero % 100)

    if (Math.sqrt(numero) === (dezena_01 + dezena_02)){

        return "É um quadrado perfeito"
    }
    else {

        return "Não é um quadrado perfeito "
    }

}
main()