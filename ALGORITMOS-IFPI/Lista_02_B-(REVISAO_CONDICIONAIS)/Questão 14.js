/**Um posto está vendendo combustíveis com a seguinte tabela de descontos:
1. Álcool:
· até 20 litros, desconto de 3% por litro
· acima de 20 litros, desconto de 5% por litro
2. Gasolina:
· até 20 litros, desconto de 4% por litro
· acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. */

import { question } from "readline-sync";
import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Calculando custo de abastecimento #### ")

function main(){

    // Entrada

    const tipo_de_combustivel = question("Infome o tipo de combustível (G - gasolina e A - Álcool): ").toUpperCase()
    const litros = get_number("Informe a quantidade de combustivel em litros: ")

    // Processamento

    const valor_a_ser_pago = calculando_pagamento(tipo_de_combustivel, litros)

    // Saida

    console.log (valor_a_ser_pago)


}

function calculando_pagamento(tipo_de_combustivel, litros){

    if (tipo_de_combustivel === "A" && litros > 20){

        const valor = litros * (1.90 * 95/100).toFixed(2)

        return valor

    }
    else if (tipo_de_combustivel === "A" && litros <= 20){

        const valor = litros * (1.90 * 97/100).toFixed(2)

        return valor
    }
    else if (tipo_de_combustivel === "G" && litros > 20){

        const valor = litros *(2.50 * 94/100).toFixed(2)

        return valor 
    }
    else if (tipo_de_combustivel === "G" && litros <= 20){

        const valor = litros * (2.50 * 96/100).toFixed(2)

        return valor 
    }
}

main()