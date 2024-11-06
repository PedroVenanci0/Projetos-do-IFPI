// 20. Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou quarto) em que o ângulo se localiza.

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Localizando quadrante #### ")

function main(){
    
    // Entrada 

    const angulo = get_number("Informe a medida do angulo(entre 0 e 360°): ")

    // Processamento

    const Qual_o_quadrante = quadrante(angulo)

    // Saida

    console.log (Qual_o_quadrante)


}

function quadrante(angulo){

    if (angulo < 90 && angulo > 0){

        return (`O Ângulo ${angulo} se localiza no primeiro quadrante`)
    }

    else if (angulo > 90 && angulo <= 180){

        return (`O Ângulo ${angulo} se localiza no segundo quadrante`)
    }

    else if (angulo > 180 && angulo <= 270 ){

        return (`O Ângulo ${angulo} se localiza no terceiro quadrante`)
    }

    else if (angulo > 270 && angulo <= 360){

        return (`O Ângulo ${angulo} se localiza no quarto quadrante`)  
    }


}
main()