// 24. Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. Vale lembrar que o coeficiente A deve ser diferente de 0 (zero).

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Raizes de uma equação #### ")

function main(){

    // Entrada

    const coeficiente_A = get_number("Informe o coeficiente A da equação de 2° grau:  ")
    const coeficiente_B = get_number("Informe o coeficiente B da equação de 2° grau:  ")
    const coeficiente_C = get_number("Informe o coeficiente C da equação de 2° grau:  ")

    // Procecssamento

    const raizes = calculando_raizes(coeficiente_A, coeficiente_B, coeficiente_C)

    // Saida

    console.log (raizes)



}
function calculando_raizes(A, B, C){

    if (A === 0){

    return ("Valor de A é inválido")
    }

    const delta = ((B**2) - 4 * A * C)

    if (delta < 0){

        return ("NÃO EXISTE RAIZES REAIS")
    }

    const bhaskara_POSITIVO = ((- B + (Math.sqrt(delta))) / 2 * A).toFixed(2)

    const bhaskara_NEGATIVO = ((- B - (Math.sqrt(delta))) / 2 * A).toFixed(2)

    return (`A primeira raiz da equação é ${bhaskara_POSITIVO}, já a segunda é ${bhaskara_NEGATIVO}`)

}
main()