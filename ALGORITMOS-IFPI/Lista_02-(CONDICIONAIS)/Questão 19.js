// 19. Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea (IMC = peso / altura2).
// Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso (IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).


import { get_number } from "../Exportar/io_utils.js"

console.log (" #### Calculando IMC (índice de massa corpórea) ")

function main(){


// Entrada 

const altura = get_number("Informe sua Altura(em metros): ")
const peso = get_number("Informe seu peso(em Kg): ")

// Processamento 

const Qual_seu_IMC = classificaçao_do_IMC(altura, peso)

// Saida

console.log (Qual_seu_IMC)

}
function classificaçao_do_IMC(altura, peso){

    const IMC = (peso / (altura**2))

    if (IMC < 25){

    return ("Peso NORMAL")
    }
    else if (IMC > 25 && IMC < 30){

    return ("Obeso")
    }
    else if (IMC > 30){

    return ("Obesidade mórbida")
    }

    
}
main()