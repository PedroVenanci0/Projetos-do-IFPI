/**O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
Até 5 Kg Acima de 5 Kg
File R$ 4,90 por Kg R$ 5,80 por Kg
Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
Picanha R$ 6,90 por Kg R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
cliente receberá ainda um desconto de 5% sobre o total a compra. Escreva um programa que peça o tipo
e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. */

import { question } from "readline-sync";
import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Compras de carne no Hipermercado Tabajara #### ")

function main(){

    // Entrada

    console.log ("Dígite F para File, A para Alcatra e P para Picanha")

    const tipo_de_carne = question("Informe o termo correspondente ao tipo de carne escolhida: ").toUpperCase()
    const quantidade_de_carne = get_number("Informe a quantidade (em kg) de carne: ")
    const cartao_tabajara = question("Informe se a compra foi deita no cartão Tabajara (S OU N): ").toUpperCase()

    // processamento 

    const preço_final = valor_a_ser_pago(tipo_de_carne, quantidade_de_carne, cartao_tabajara)

    const desconto_cartao = calculando_desconto(tipo_de_carne, quantidade_de_carne, cartao_tabajara)

    const como_foi_pago = tipo_de_pagamento(cartao_tabajara)

    const preço_sem_desconto = preço_bruto(tipo_de_carne, quantidade_de_carne)

    const a_carne_escolhida_foi = carne(tipo_de_carne)

    // Saida

    console.log 
    
    (`

        ----------------------

        **** Cumpom fiscal ****

        . Tipo de carne: ${a_carne_escolhida_foi}

        . Quantidade de carne: ${quantidade_de_carne} Kg

        . Preço total (preço sem desconto): ${preço_sem_desconto} REAIS

        . Tipo de pagamento: ${como_foi_pago}

        . Valor do desconto: ${desconto_cartao}

        . Valor a pagar: ${preço_final} REAIS

        -----------------------


        
        
    `)

    
    


}

function preço_bruto(tipo_de_carne, quantidade_de_carne){

    const File_menor = quantidade_de_carne * 4.90

    const File_maior = quantidade_de_carne * 5.80

    const alcatra_menor = quantidade_de_carne * 5.90

    const alcatra_maior = quantidade_de_carne * 6.80

    const picanha_menor = quantidade_de_carne * 6.90

    const picanha_maior = quantidade_de_carne * 7.80


    if (tipo_de_carne === "F" && quantidade_de_carne <= 5){

        return File_menor
    }

    else if (tipo_de_carne === "F" && quantidade_de_carne > 5 ){

        return File_maior
    }

    else if (tipo_de_carne === "A" && quantidade_de_carne <= 5 ){

        return alcatra_menor
    }

    else if (tipo_de_carne === "A" && quantidade_de_carne > 5 ){

        return alcatra_maior
    }

    else if (tipo_de_carne === "P" && quantidade_de_carne <= 5 ){

        return picanha_menor
    }

    else if (tipo_de_carne === "P" && quantidade_de_carne > 5 ){

        return picanha_maior
    }

}

function valor_a_ser_pago(tipo_de_carne, quantidade_de_carne, cartao_tabajara){

    const File_menor = quantidade_de_carne * 4.90

    const File_maior = quantidade_de_carne * 5.80

    const alcatra_menor = quantidade_de_carne * 5.90

    const alcatra_maior = quantidade_de_carne * 6.80

    const picanha_menor = quantidade_de_carne * 6.90

    const picanha_maior = quantidade_de_carne * 7.80

    if (tipo_de_carne === "F" && quantidade_de_carne <= 5 && cartao_tabajara === "N"){

        return File_menor
    }

    else if (tipo_de_carne === "F" && quantidade_de_carne > 5 && cartao_tabajara === "N"){

        return File_maior
    }

    else if (tipo_de_carne === "A" && quantidade_de_carne <= 5 && cartao_tabajara === "N"){

        return alcatra_menor
    }

    else if (tipo_de_carne === "A" && quantidade_de_carne > 5 && cartao_tabajara === "N"){

        return alcatra_maior
    }

    else if (tipo_de_carne === "P" && quantidade_de_carne <= 5 && cartao_tabajara === "N"){

        return picanha_menor
    }

    else if (tipo_de_carne === "P" && quantidade_de_carne > 5 && cartao_tabajara === "N"){

        return picanha_maior
    }


    else if (tipo_de_carne === "F" && quantidade_de_carne <= 5 && cartao_tabajara === "S"){

        const compra_cartao = File_menor * 95/100

        return compra_cartao
    }

    else if (tipo_de_carne === "F" && quantidade_de_carne > 5 && cartao_tabajara === "S"){

        const compra_cartao = File_maior * 95/100

        return compra_cartao
    }

    else if (tipo_de_carne === "A" && quantidade_de_carne <= 5 && cartao_tabajara === "S"){

        const compra_cartao = alcatra_menor * 95/100

        return compra_cartao
    }

    else if (tipo_de_carne === "A" && quantidade_de_carne > 5 && cartao_tabajara === "S"){

        const compra_cartao = alcatra_maior * 95/100

        return compra_cartao
    }

    else if (tipo_de_carne === "P" && quantidade_de_carne <= 5 && cartao_tabajara === "S"){

        const compra_cartao = picanha_menor * 95/100

        return compra_cartao
    }

    else if (tipo_de_carne === "P" && quantidade_de_carne > 5 && cartao_tabajara === "S"){

        const compra_cartao = picanha_maior * 95/100

        return compra_cartao
        
    }


}

function carne(tipo_de_carne){

    if (tipo_de_carne === "F"){

        return "Filé"

    }
    else if (tipo_de_carne === "A"){

        return "Alcatra"

    }
    else if (tipo_de_carne === "P"){

        return "Picanha"

    }
}

function tipo_de_pagamento(cartao_tabajara){

    if ( cartao_tabajara === "S"){

        return "Pago com Cartão Tabajara"

    }
    else {

        return "Pago sem o Cartão Tabajara"
    }
}

function calculando_desconto(tipo_de_carne, quantidade_de_carne, cartao_tabajara){

    const File_menor = quantidade_de_carne * 4.90

    const File_maior = quantidade_de_carne * 5.80

    const alcatra_menor = quantidade_de_carne * 5.90

    const alcatra_maior = quantidade_de_carne * 6.80

    const picanha_menor = quantidade_de_carne * 6.90

    const picanha_maior = quantidade_de_carne * 7.80



     if (tipo_de_carne === "F" && quantidade_de_carne <= 5 && cartao_tabajara === "S"){

        const valor_do_desconto = File_menor * 5/100

        return valor_do_desconto

        
    }

    else if (tipo_de_carne === "F" && quantidade_de_carne > 5 && cartao_tabajara === "S"){

        const valor_do_desconto = File_maior * 5/100

        return valor_do_desconto
    }

    else if (tipo_de_carne === "A" && quantidade_de_carne <= 5 && cartao_tabajara === "S"){

        const valor_do_desconto = alcatra_menor * 5/100

        return valor_do_desconto
    }

    else if (tipo_de_carne === "A" && quantidade_de_carne > 5 && cartao_tabajara === "S"){

        const  valor_do_desconto = alcatra_maior * 5/100

        return valor_do_desconto
    }

    else if (tipo_de_carne === "P" && quantidade_de_carne <= 5 && cartao_tabajara === "S"){

        const valor_do_desconto = picanha_menor * 5/100

        return valor_do_desconto
    }

    else if (tipo_de_carne === "P" && quantidade_de_carne > 5 && cartao_tabajara === "S"){

        const valor_do_desconto = picanha_maior * 5/100

        return valor_do_desconto
        
    }

    else {

        return "SEM DESCONTO"
    }

}

main()