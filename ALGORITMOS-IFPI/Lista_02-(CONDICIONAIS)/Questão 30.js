// Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: 
// se dividirmos o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
// milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
// terceiro número é exatamente o número original de quatro dígitos. 
// Por exemplo:  2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025.

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### retomando o numero original #### ")

function main(){

    // Entrada

    const numero = get_number("Informe um número de 4 dígitos: ")

    // Processamento

    const numero_original = original(numero)

    // Saida

    console.log (numero_original)

}

function original(numero){

    if (numero >= 1000 && numero <= 9999 ){

    }

    const dividindo_milhar = Math.trunc(numero / 100)
    const dividindo_dezena = Math.trunc(numero % 100)

    const somatorio = dividindo_dezena + dividindo_milhar

    const quadrado = somatorio**2

    if (quadrado === numero){

        return `O quadrado da soma dos termos é igual ao número original`
    }
}

main()