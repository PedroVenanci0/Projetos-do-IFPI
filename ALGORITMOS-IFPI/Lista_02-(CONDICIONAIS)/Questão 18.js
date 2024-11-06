// 18. Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 –Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). 
// Calcule e escreva o resultado dessa operação sobre os dois valores lidos.

import { question } from "readline-sync";

console.log (" #### Executanto Operações #### ")

function main (){

    // Entrada

console.log ("Número das operações:  1 -> Adição, 2 -> Subtração, 3 -> Multiplicação e 4 -> Divisão)")

    const valor_01 = Number(question("Informe o primeiro valor: "))
    const valor_02 = Number(question("Informe o segundo valor: "))
    const opção = Number(question("Informe o número da operação a ser usada: "))

    // Processamento

    const Qual_a_operação = operação(valor_01, valor_02, opção)

    // Saida

    console.log (Qual_a_operação)


}

function operação(valor_01, valor_02, opção){

  if (opção === 1){

    return (adiçao(valor_01, valor_02))
}
  else if (opção === 2){

    return  (subtracao(valor_01, valor_02))  

}
  else if (opção === 3){

    return (multiplicacao(valor_01, valor_02))

} 
  else if (opção === 4){

    return (divisao(valor_01, valor_02))
}

  else (opção !== 1 && opção !== 2 && opção !== 3 && opção !== 4) 

    return ("Valor da opção é INVÁLIDO")


}

function adiçao(v1, v2){

    const somatorio =  v1 + v2

    return (`A adição dos termos é igual a ${somatorio}`)
}

function subtracao(v1, v2){

    const subtrair = v1 - v2

    return (`A subtração dos termos é igual a ${subtrair}`)
}

function multiplicacao(v1, v2){

    const multiplicar = v1 * v2

    return (`A multiplicação dos termos é igual a ${multiplicar} `)
}

function divisao(v1, v2){

    const dividir = v1 / v2

    return (`A divisão dos termos é igual a ${dividir}`)
}

main()