// 7. Leia 3 (três) números (cada número corresponde a um lado do triângulo), 
// verifique e escreva se os 3 (três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). 
// Se formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).

import { get_positivo_number, print } from "../Exportar/io_utils.js"

function main(){

    const numero_01 = get_positivo_number("Qual o valor do primeiro lado do triângulo:  ")
    const numero_02 = get_positivo_number("Qual o valor do segundo lado do triângulo:  ")
    const numero_03 = get_positivo_number("Qual o valor do terceiro lado do triângulo:  ")

    if (verificação_de_triangulos(numero_01, numero_02, numero_03)){

        print ("É um triângulo")

    const  classificação = classificar_triangulo(numero_01, numero_02, numero_03)

        print (`Esse triângulo é classificado como ${classificação}`)


}

function verificação_de_triangulos(numero_01, numero_02, numero_03){

    if ((numero_01 + numero_02) > numero_03 || (numero_02 + numero_03) > numero_01 || (numero_01 + numero_03) > numero_02)
    
    return ('É um triângulo')

    else {
        
        print ("Não é um triângulo")

    }
}

function classificar_triangulo(numero_01, numero_02, numero_03){

    if (numero_01 === numero_02 && numero_01 === numero_03 && numero_02 === numero_03){

        return ("Equilátero")


    } else if ((numero_01 === numero_02) && numero_01 !== numero_03 || (numero_01 === numero_03) && numero_01 !== numero_02 || (numero_03 === numero_02) && numero_01 !== numero_01){

        return ("Isósceles")
    }

      else if (numero_01 !== numero_02 !== numero_03)

         return ("Escaleno")

}
}
main()
