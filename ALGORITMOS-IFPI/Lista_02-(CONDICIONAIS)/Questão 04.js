// 4. Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente do algarismo da unidade.

import { question } from "readline-sync"

import { print } from "../Exportar/io_utils.js"


function main(){


    const numero = get_positivo_number ("Informe um número de no maximo dois digitos: ")

    print (verificando_igualdade(numero))

}


function verificando_igualdade(numero){


    if ( Math.trunc(numero / 10) !== (Math.trunc(numero % 10)))

    return (`Os algarismos que representam Dezena e Unidade são diferentes`)
   
    else if (Math.trunc(numero / 10) === (Math.trunc(numero % 10)))

    return (`Os algarismos que representam Dezena e Unidade são iguais `)

    

}

function get_positivo_number(mensagem){

    const numero = get_number(mensagem)
  
    if (numero > 99 ){

      print ('Número maior que 2 dígitos! Por favor dígite novamente.')

      return get_positivo_number(mensagem)
    }
  
    return numero

}

function get_number(mensagem){
    return Number(question(mensagem))
  }




main()