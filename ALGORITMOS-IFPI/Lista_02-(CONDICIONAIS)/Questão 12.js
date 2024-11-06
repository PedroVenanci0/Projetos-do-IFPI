// 12. Leia 1 (um) número inteiro e escreva se este número é par ou impar.

import { question } from "readline-sync";

console.log (" #### É par ou impar #### ")

function main(){

    // Entrada

    const numero_inteiro = Number(question("Informe um número inteiro: "))

    // processamento 

    const validando =  par_ou_impar(numero_inteiro)
    

    // Saida 

    console.log (`O número inteiro ${numero_inteiro} é ${validando} `)





function par_ou_impar(numero_inteiro){

    if (numero_inteiro % 2 === 0){

    return ("Par")

    }else{ 

    return ("impar")
    }
}


}
main()

