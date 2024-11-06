// 13. Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes.

import { question } from "readline-sync";

function main(){

    console.log ("#### maior e menor número ####")

    // Entrada 

    console.log("Explane 5 números diferentes")

    const num_1 = Number(question("Informe o primeiro número: "))
    const num_2 = Number(question("Informe o segundo número: "))
    const num_3 = Number(question("Informe o terceiro número: "))
    const num_4 = Number(question("Informe o quarto número: "))
    const num_5 = Number(question("Informe o quinto número: "))

   // Processamento
   
   const maior = (Identificando_maior(num_1, num_2, num_3, num_4, num_5))
   const menor = (Identificando_menor(num_1, num_2, num_3, num_4, num_5))

   // Saida

   console.log (`O maior número é ${maior} e o menor número é ${menor}`)
}
function Identificando_maior(n1, n2, n3, n4, n5){


    if (n1 > n2 && n1 > n3 && n1 > n4 && n1 > n5)

    return n1

    else if (n2 > n1 && n2 > n3 && n2 > n4 && n2 > n5)

    return n2

    else if (n3 > n2 && n3 > n1 && n3 > n4 && n3 > n5)

    return n3

    else if (n4 > n2 && n4 > n3 && n4 > n1 && n4 > n5)

    return n4

    else if (n5 > n2 && n5 > n3 && n5 > n4 && n5 > n1)

    return n5
    


}

function Identificando_menor(n1, n2, n3, n4, n5){

    
    if (n1 < n2 && n1 < n3 && n1 < n4 && n1 < n5)

    return n1

    else if (n2 < n1 && n2 < n3 && n2 < n4 && n2 < n5)

    return n2

    else if (n3 < n2 && n3 < n1 && n3 < n4 && n3 < n5)

    return n3

    else if (n4 < n2 && n4 < n3 && n4 < n1 && n4 < n5)

    return n4

    else if (n5 < n2 && n5 < n3 && n5 < n4 && n5 < n1)

    return n5



}


main()