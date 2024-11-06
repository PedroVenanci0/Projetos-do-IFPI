/**Uma fruteira está vendendo frutas com a seguinte tabela de preços:
Até 5 Kg Acima de 5 Kg
Morango R$ 2,50 por Kg R$ 2,20 por Kg
Maçã R$ 1,80 por Kg R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. */

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Preço do carrinho de frutas #### ")

function main(){

    // Entrada 

    const morangos = get_number("Informe a quantidade de morangos (em Kg): ")
    const maças = get_number("Informe a quantidade de maçãs (em Kg): ")

    // Processamento 

    const preço_final =  calculando_preço(morangos, maças)

    // Saida

    console.log (` O preço a ser pago pela compra das frutas é ${preço_final} reais`)

}

function calculando_preço(morangos, maças){

    const quantidade = morangos + maças

    const quantidade_preço_alto = (morangos * 2.20) + (maças * 1.50)

    if (quantidade <= 5 ){

        let preço_morango = morangos * 2.50

        let preço_maças = maças * 1.80

        let preço_pago = preço_maças + preço_morango

        return preço_pago


    }
    else if (quantidade > 5 && quantidade <= 8){

        let preço_morango = morangos * 2.20

        let preço_maças = maças * 1.50

        let preço_pago = preço_maças + preço_morango

        return preço_pago 
    }

    else if (quantidade > 8 || quantidade_preço_alto > 25 ){

        let preço_morango = morangos * 2.20

        let preço_maças = maças * 1.50

        let preço_pago = (preço_maças + preço_morango) * 90/100

        return preço_pago

    }
}

main()