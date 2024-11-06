// 6. Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
// se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). 
// Se formam, verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).

import { get_positivo_number, print } from "../Exportar/io_utils.js"

function main(){

    const numero_01 = get_positivo_number("Informe o primeiro ângulo do triângulo: ")
    const numero_02 = get_positivo_number("Informe o segundo ângulo do triângulo: ")
    const numero_03 = get_positivo_number("Informe o terceiro ângulo do triângulo: ")

    if (verificação_de_triangulos(numero_01, numero_02, numero_03)){

    print ("É um triângulo")

    const classificação = classificação_triangulo(numero_01, numero_02, numero_03)
      
    print (`E sua classificação é ${classificação}`)

        } else{
        
        print ("Não é um triângulo")
    
        }
}

function verificação_de_triangulos(numero_01, numero_02, numero_03){

   return (numero_01 + numero_02 + numero_03 === 180)
   
}

function classificação_triangulo(numero_01, numero_02, numero_03){

    if (numero_01 < 90 && numero_02 < 90 && numero_03 < 90){

    return ("Acutângulo")

}

    else if (numero_01 === 90 || numero_02 === 90 || numero_03 === 90 ){

    return ("Retângulo")

}

    else if (numero_01 > 90 || numero_02 > 90 || numero_03 > 90){

    return ("Obtuângulo")

 }





}

main()