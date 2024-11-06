// 11. Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; 
// o valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3.
// Os únicos valores possíveis para a variável opção são 1, 2 e 3.

import { question } from "readline-sync";

console.log (" #### Identificação de números idênticos #### ")

function main(){

    // Entrada

    
    console.log (" A opção númerica deve ser entre 1 e 3")
    const opção = Number(question("Informe uma opção númerica: "))
    

    const num_1 =  Number(question("Informe o valor primeiro número: "))
    const num_2 =  Number(question("Informe o valor segundo número: "))
    const num_3 =  Number(question("Informe o valor terceiro número: "))

    const verifique = verificando(opção)
    const idênticos = Identificando(opção, num_1, num_2, num_3)
    

    // processamento 

function Identificando(opção, num_1, num_2, num_3){

    if (opção === 1)

    return num_1

    else if (opção === 2)

    return num_2

    else if (opção === 3)

    return num_3


}

function verificando(opção){

    if (opção > 3 || opção < 1)

    return "O valor da opção númerica esta inválido"
}

    // saida

    console.log ( verifique || idênticos)
    

    








}
 main()

