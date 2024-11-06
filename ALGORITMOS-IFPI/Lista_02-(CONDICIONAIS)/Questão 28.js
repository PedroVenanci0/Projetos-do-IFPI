// 28. Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de um retângulo.
// Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área não pode ser negativo.

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Área do retângulo #### ")

function main(){

    // Entrada 

    const ponto_01_base = get_number("Informe o ponto X: ")
    const ponto_02_altura = get_number("Informe o ponto Y: ")

    // Processamento

    const area = calculando_area(ponto_01_base, ponto_02_altura)

    // Saida

    console.log (`A área do retângulo é igual a ${area}`)

}

function calculando_area(p1, p2){

    const area_do_retangulo = p1 * p2

    return area_do_retangulo

    


}

main()